from qingcloud.iaas import APIConnection
import yaml
import datetime
def removdoublelist(items):
    for item in items:
        if isinstance(item,list):
            items.remove(item)
    return items

def handledata(ret):
    cpu_maxvalue = None
    cpu_avgvalue = None
    mem_maxvalue = None
    mem_avgvalue = None
    disk_read_maxvalue = None
    disk_read_avgvalue = None
    disk_write_maxvalue = None
    disk_write_avgvalue = None
    if ret['meter_set']:
        for items in ret['meter_set']:
            if not items['data']:
                continue
            data_list= removdoublelist(items['data'])
            if items['meter_id'] == 'cpu':
                try:
                    cpu_maxvalue = max(data_list)/10
                    cpu_avgvalue = sum(data_list)/len(data_list)/10
                except:
                    cpu_maxvalue = None
                    cpu_avgvalue = None
            elif items['meter_id'] == 'memory':
                try:
                    mem_maxvalue = max(data_list)/10
                    mem_avgvalue = sum(data_list)/len(data_list)/10
                except:
                    mem_maxvalue = None
                    mem_avgvalue = None

            elif items['meter_id'] == 'disk-iops-os':
                try:
                    disk_read = removdoublelist([x[0] for x in data_list])
                    disk_read_maxvalue = max(disk_read)
                    disk_read_avgvalue = sum(disk_read)/len(disk_read)
                    disk_write = removdoublelist([x[1] for x in data_list])
                    disk_write_maxvalue = max(disk_write)
                    disk_write_avgvalue = sum(disk_write)/len(disk_write)
                except:
                    disk_read_maxvalue = None
                    disk_read_avgvalue = None
                    disk_write_maxvalue = None
                    disk_write_avgvalue = None
            else:
                pass
    return (cpu_maxvalue, cpu_avgvalue,
            mem_maxvalue, mem_avgvalue,
            disk_read_maxvalue, disk_read_avgvalue,
            disk_write_maxvalue, disk_write_avgvalue)

with open('qingcloud.yaml') as f:
    configs = yaml.load(f.read())

zone = configs.get('zone')
access_key_id = configs.get('access_key_id')
secret_access_key = configs.get('secret_access_key')
host = configs.get('host')

conn = APIConnection(access_key_id, secret_access_key,zone,host=host,port='7777',protocol='http')
nowtime = datetime.datetime.now()
start_one_time = (nowtime + datetime.timedelta(days=-1)).strftime('%Y-%m-%dT%H:%M:%SZ')
start_sev_time = (nowtime + datetime.timedelta(days=-7)).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = nowtime.strftime('%Y-%m-%dT%H:%M:%SZ')
g = open('instance_list')
for line in g.readlines():
    instance_id = line.strip()
    one_day_ret = conn.get_monitoring_data(instance_id ,['cpu','memory','disk-iops-os'],'5m', start_one_time, end_time)
    sev_day_ret = conn.get_monitoring_data(instance_id ,['cpu','memory','disk-iops-os'],'5m', start_sev_time, end_time)
    one_day_result_list = handledata(one_day_ret)
    sev_day_result_list = handledata(sev_day_ret)
    print "instance_id:%s, one day: %s, 7 day: %s"%(instance_id,str(one_day_result_list),str(sev_day_result_list))