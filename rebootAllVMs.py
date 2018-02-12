#!/usr/bin/env python3


import pexpect


TIMEOUT=2

hosts=['172.16.115.32', '172.16.115.31', '172.16.115.33']


for host in hosts:
    cmd="ssh " + "-l " + "vyos " + host
    print('[+] rebooting host: ', host)

    child = pexpect.spawnu(cmd, timeout=int(TIMEOUT))
    child.expect ('.*assword:')
    child.sendline ('vyatta')
    child.expect('.*router00')
    child.sendline ('reboot')
    child.expect('.*roceed with reboot')
    child.sendline ('Yes')
    child.sendline ('\r\n')
    child.sendline ('\r\n')



