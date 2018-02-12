#!/usr/bin/env python3


import pexpect


logFile=open("myLog001.txt", "a")
#print(type(logFile))
#Note: py3 / py2 issues writing to file (write bytes vs string)


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




"""
Fork this later / alt call from a different module

child1 = pexpect.spawnu('ssh -l vyos 172.16.115.31', timeout=200)
child1.expect ('.*assword:')
child1.sendline ('vyatta')

child3 = pexpect.spawnu('ssh -l vyos 172.16.115.33', timeout=200)
child3.expect ('.*assword:')
child3.sendline ('vyatta')
"""
