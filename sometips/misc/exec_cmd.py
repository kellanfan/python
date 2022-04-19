# -*- coding: utf-8 -*-

import subprocess

def exec_cmd(cmd, remote_host=None):
    if remote_host is not None:
        # $ means to get the value in shell
        cmd = cmd.replace("$", "\$")
        cmd = "ssh -o 'StrictHostKeyChecking no' -o 'UserKnownHostsFile ~/.ssh/known_hosts' -o ConnectTimeout=10 -o ConnectionAttempts=3 \
            root@{0} \"{1}\"".format(remote_host, cmd)

    p = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # get the result
    out, err = p.communicate()
    code = p.returncode
    out = out.strip()
    err = err.strip()
    if code != 0 and err:
        result = {'code': code, 'out': '', 'err': err}
    else:
        result = {'code': code, 'out': out, 'err': err}
    return result
