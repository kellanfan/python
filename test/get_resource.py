'''
Created on 2013-08-02

@author: yunify
'''
import sys
sys.path.append("/pitrix/lib/pitrix-common")
sys.path.append("/pitrix/lib/pitrix-cli")
sys.path.append("/pitrix/lib/pitrix-scripts")

import context
from optparse import OptionParser
from misc.utils import load_conf
from utils.global_conf import get_pg
from db.constants import DB_ZONE
from utils.id_tool import get_resource_type

def _get_opt_parser():
    ''' get option parser '''
    
    MSG_USAGE = '''%prog [-f <conf_file>]'''
    opt_parser = OptionParser(MSG_USAGE)
         
    opt_parser.add_option("-r", "--resource_id", action = "store", type = "string", 
            dest = "resource_id", help='the ID of resource', default="")
         
    opt_parser.add_option("-f", "--config", action = "store", type = "string", 
            dest = "conf_file", help='config file of your access keys', default="/pitrix/conf/client.yaml") 
 
    return opt_parser

UUID_TYPE_IMAGE = "img"
UUID_TYPE_INSTANCE = "i"
UUID_TYPE_JOB = "j"
UUID_TYPE_TASK = "t"
UUID_TYPE_VXNET = "vxnet"
UUID_TYPE_VOLUME = "vol"
UUID_TYPE_MASS_VOLUME = "vom"
UUID_TYPE_KEYPAIR = "kp"
UUID_TYPE_SECURITY_GROUP = "sg"
UUID_TYPE_SECURITY_GROUP_RULE = "sgr"
UUID_TYPE_CONTRACT = "ct"
UUID_TYPE_TICKET = "tk"
UUID_TYPE_TICKET_REPLY = "tkr"
UUID_TYPE_TICKET_ATTACHMENT = "tka"
UUID_TYPE_TICKET_TEMPLATE = "tkt"
UUID_TYPE_PRICE_KEY = "pk"
UUID_TYPE_EIP = "eip"
UUID_TYPE_USER = "usr"
UUID_TYPE_DISCOUNT = "dc"
UUID_TYPE_RECHARGE = "rchg"
UUID_TYPE_TRADE = "tr"
UUID_TYPE_INVOICE = "invc"
UUID_TYPE_ROUTER = "rtr"
UUID_TYPE_ROUTER_STATIC = "rtrs"
UUID_TYPE_EIP_GROUP = "eipg"
UUID_TYPE_INSTANCE_SAVEVM = "ivm"
UUID_TYPE_EMAIL_JOB = "ejob"
UUID_TYPE_SMS_JOB = "sms"
UUID_TYPE_RDB = "rdb"
UUID_TYPE_RDB_MYSQL_INSTANCE = "rmi"
UUID_TYPE_LOADBALANCER = "lb"
UUID_TYPE_LB_LISTENER = "lbl"
UUID_TYPE_LB_BACKEND = "lbb"
UUID_TYPE_SNAPSHOT = "ss"
UUID_TYPE_ROUTER_STATIC_ENTRY = "rse"
UUID_TYPE_BANDWIDTH = "bw"
UUID_TYPE_EIP_COUNT = "eipc"
UUID_TYPE_LB_POLICY = "lbp"
UUID_TYPE_LB_POLICY_RULE = "lbpr"

def get_resource_type(uuid, verbose=1):
    ''' get resource type '''
    prefix = uuid.split("-")[0] 
    if prefix == UUID_TYPE_INSTANCE:
        return "instance"
    elif prefix == UUID_TYPE_IMAGE:
        return "image"
    elif prefix == UUID_TYPE_VOLUME:
        return "volume"
    elif prefix == UUID_TYPE_MASS_VOLUME:
        if verbose == 0:
            return "volume"
        else:
            return "mass_volume"
    elif prefix == UUID_TYPE_EIP:
        return "eip"
    elif prefix == UUID_TYPE_ROUTER:
        return "router"
    elif prefix == UUID_TYPE_VXNET:
        return "vxnet"
    elif prefix == UUID_TYPE_INSTANCE_SAVEVM:
        return "savevm"
    elif prefix == UUID_TYPE_LOADBALANCER:
        return "loadbalancer"
    elif prefix == UUID_TYPE_LB_LISTENER:
        return "loadbalancer_listener"
    elif prefix == UUID_TYPE_LB_BACKEND:
        return "loadbalancer_backend"
    elif prefix == UUID_TYPE_SNAPSHOT:
        return "snapshot"
    elif prefix == UUID_TYPE_BANDWIDTH:
        return "bandwidth"
    elif prefix == UUID_TYPE_EIP_COUNT:
        return "eip_count"
    elif prefix == UUID_TYPE_RDB:
        return "rdb"
    elif prefix == UUID_TYPE_KEYPAIR:
        return "keypair"
    elif prefix == UUID_TYPE_SECURITY_GROUP:
        return "security_group"
    # return default
    return "image"

def build_sql(table, resource):
    if table == 'keypair':
        table = 'key_pair'
    if table == 'security_group':
        resource.update({'is_default':0})
    
    # build sql
    sql = "insert into %s" % table
    (col_names, val_names, parameters) = ("", "", [])
    for k, v in resource.items():
        if k.find('_time') >= 0:
            print "ignore column [%s]" % k
            continue
        if len(parameters) == 0:
            col_names += "(%s" % k
            if isinstance(v, int):
                val_names += "(%s" % v
            else:
                val_names += "(\'%s\'" % v
        else:
            col_names += ", %s" % k
            if isinstance(v, int):
                val_names += ", %s" % v
            else:
                val_names += ", \'%s\'" % v
        parameters.append(v)
    sql += " %s) values %s);" % (col_names, val_names)
    print sql
    
    return

def get_resource(resource_id):
    ctx = context.instance()
    
    # check resource type
    resource_type = get_resource_type(resource_id, verbose=0)
    if resource_type not in ['instance', 'volume', 'image', 'snapshot', 'keypair', 'security_group']:
        print "illegal resource type [%s]" % resource_type
        return -1
    
    # get resource
    if resource_type == 'keypair':
        sql = "select * from %s where %s_id = \'%s\' limit 1;" % ('key_pair', 'keypair', resource_id)
    elif resource_type == 'security_group':
        sql = "select * from %s where %s_id = \'%s\' limit 1;" % ('security_group', 'group', resource_id)
    else:
        sql = "select * from %s where %s_id = \'%s\' limit 1;" % (resource_type, resource_type, resource_id)
    res_set = ctx.pg.execute_sql(sql, [])
    if res_set is None or len(res_set) == 0:
        print "get [%s] failed" % resource_id
        return -1
    resource = res_set[0]
    
    # build sql
    build_sql(resource_type, resource)
    
    if resource_type == 'snapshot':
        sql = "select * from %s where snapshot_id = \'%s\' limit 1;" % ('snapshot_resource', resource_id)
        res_set = ctx.pg.execute_sql(sql, [])
        if res_set is None or len(res_set) == 0:
            print "get [%s] failed" % resource_id
            return -1
        resource = res_set[0]        
    
        # build sql
        build_sql('snapshot_resource', resource)
        
    if resource_type == 'security_group':
        sql = "select * from %s where group_id = \'%s\' limit 50;" % ('security_group_rules', resource_id)
        res_set = ctx.pg.execute_sql(sql, [])
        if res_set is None or len(res_set) == 0:
            print "get [%s] failed" % resource_id
            return -1
        resources = res_set        
    
        # build sql
        for resource in resources:
            build_sql('security_group_rules', resource)
             
    return 0

def main(args):
    # parser options
    parser = _get_opt_parser()
    (options, _) = parser.parse_args(args)
             
    # load conf
    pitrix_conf = load_conf(options.conf_file)
    if pitrix_conf is None:
        print "load conf file [%s] failed" % options.conf_file
        sys.exit(-1)
        
    # connect to postgresql db
    pg = get_pg(DB_ZONE)      
    if pg == None:
        print "connect to PostgreSQL zone failed: can't connect"
        sys.exit(-1)
        
    # init context
    ctx = context.instance()
    ctx.pg = pg
    
    # get argument
    resource_id = options.resource_id
    
    # update
    ret = get_resource(resource_id)
    sys.exit(ret)

if __name__ == '__main__':
    main(sys.argv[1:])