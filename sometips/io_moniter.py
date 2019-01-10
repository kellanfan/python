import os
import time
def check_io():
    flog = open('/var/log/io_rate.log','a+')

    cmd = """/usr/sbin/iotop -P -b -n 1 -o |awk '{for (i=12;i<=NF;i++)printf("%s %s %s ", $1,$10,$i);print ""}'|grep ^[0-9]"""

    temp = os.popen(cmd).read()
    if temp:
        l_temp = filter(None,temp.split('\n'))
        for line in l_temp:
            pid_name = ' '.join(line.split()[2::3])
            pid = line.split()[0]
            io_rate = line.split()[1].split('.')[0]
            log_msg = "%s ### %s %s"%(time.ctime(),io_rate,pid_name)
            flog.write(log_msg+'\n')
            if int(io_rate) > 50:
                f = open('.curr_status_io_rate','a+')
                msg = "pid %s , process_name: %s , iorate: %s"%(pid, pid_name, io_rate)
                f.write(msg+'\n')
                f.close()
    flog.close()
            
def mk_letter():
    hostname = os.popen('hostname').read().split('\n')[0]
    now = time.strftime('%H%M%S',time.localtime(time.time()))
    filename = 'alert_agent_%s_%s'%(hostname,now)
    f = open(filename,'w')
    f.write('[tzcs] [%s] has alerts \n\n'%hostname)
    f.write('<h2>[tzcs] [%s] has alerts</h2>\n'%hostname)
    f.write('<br>\n')
    f.write('<h3>=== io_rate ===</h3>\n')
    for line in open('.curr_status_io_rate'):
        f.write('<p>%s</p>\n'%line)
    f.write('<br>')
    f.close()
    os.system('touch %s.sign'%filename)
    os.system('scp %s proxy:/pitrix/notifier/'%filename)
    os.system('scp %s.sign proxy:/pitrix/notifier/'%filename)
    os.rename('.curr_status_io_rate','.last_status_io_rate')
    os.remove(filename)
    os.remove('%s.sign'%filename)

if __name__ == '__main__':
    check_io()
    if os.path.exists('.curr_status_io_rate') and os.system('diff .curr_status_io_rate .last_status_io_rate >/dev/null') != 0:
        mk_letter()
