#!/usr/bin/env python3


import pexpect


logFile=open("myLog001.txt", "a")
#print(type(logFile))
#Note: py3 / py2 issues writing to file (write bytes vs string)


TIMEOUT=2
#child = pexpect.spawn('ssh -l vyos 172.16.115.32', logfile="./alogFile.txt")
#child = pexpect.spawnu('ssh -l vyos 172.16.115.32', logfile=logFile)
#child = pexpect.spawnu('ssh -l vyos 172.16.115.32')

child = pexpect.spawnu('ssh -l vyos 172.16.115.32', timeout=int(TIMEOUT))
child.expect ('.*assword:')
child.sendline ('vyatta')

"""
Fork this later / alt call from a different module

child1 = pexpect.spawnu('ssh -l vyos 172.16.115.31', timeout=200)
child1.expect ('.*assword:')
child1.sendline ('vyatta')

child3 = pexpect.spawnu('ssh -l vyos 172.16.115.33', timeout=200)
child3.expect ('.*assword:')
child3.sendline ('vyatta')
"""


promptR001='.*router001:'
promptR002='.*router002:'
promptR003='.*router003:'

#try 1: promptED='.*router.*\#'
#try 2: promptED='.*vyos@router002#'
promptED='.*\[edit\]'


def do_something(value):
    print('I\'m doing something.', value)


def do_some_other_thing(child):
    child.sendline('\r\n')
    child.expect (promptR002)
    child.sendline('show host name')
    child.expect (promptR002)
    child.sendline('show interface')
    child.expect (promptR002)
    child.sendline('configure')
    child.expect (promptR002)
    child.sendline('set interface ethernet eth1 description "vyETH: eth1 peer005"')
    child.expect (promptED)
    child.sendline('commit')
    child.expect (promptED)
    child.sendline('exit')

    child.expect (promptR002)
    child.sendline('\r\n')
    child.sendline('\r\n')
    child.sendline('\r\n')




def addNIntAndRouting(child, prompt):
    #child = pexpect.spawnu('ssh -l vyos 172.16.115.33', timeout=2)
    #child.expect ('.*assword:')
    #child.sendline ('vyatta')

    child.sendline('\r\n')
    child.expect (prompt)
    child.sendline('show host name')
    child.expect (prompt)
    child.sendline('show interface')
    child.expect (prompt)
    child.sendline('configure')
    child.expect (prompt)
    child.sendline('set interface ethernet eth1 description "vyETH: eth1 peer005"')
    child.expect (promptED)
    child.sendline('set interface dummy dum5 description "vyETH: dum5 192.168.5.1/24"')
    child.expect (promptED)
    child.sendline('set interface dummy dum5 address 192.168.5.1/24')
    child.expect (promptED)
    child.sendline('set protocols bgp 65532 network 192.168.5.0/24')
    child.expect (promptED)
    child.sendline('commit')
    child.expect (promptED)
    child.sendline('exit')

    child.expect (prompt)
    child.sendline('\r\n')
    child.expect (prompt)

    child.sendline('reset ip bgp all')

    child.expect (prompt)
    child.sendline('show ip bgp')
    child.sendline('\r\n')
    child.sendline('\r\n')



def verifyDescR2(child):
    child.sendline('\r\n')    
    child.expect (promptR002)

    child.sendline('show interface')
    child.expect (promptR002)

    child.sendline('show host name')
    child.expect (promptR002)

    child.sendline('show interface')
    child.expect (promptR002)

    child.sendline('\r\n')    
    child.expect (promptR002)

    child.sendline('show interface')
    index = child.expect(['reallyNeverExpectTHISSKIPTHISOUPUT', '.*vyETH: eth1 peer005', promptR002, pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        #do_something('001')
        pass 
    elif index == 1:
        #do_something_else('002')
        #do_something('002')
        print('[+] Test for ', promptR002, ' description ', 'passed')
        print('[S] match string: ', child.match.string)
        pass
    elif index == 2:
        print('[-] Test for ', promptR002, ' description ', 'failed')


    child.sendline('\r\n')    
    child.expect (promptR002)
    child.sendline('\r\n')    
     
def exitDevice(child):
    print('[*] Exiting ')
    child.sendline('\r\n')    
    child.expect (promptR002)
    child.sendline('exit')    
    child.sendline('\r\n')    
    
def chkBGPASN(child):
    ##child.expect('.*router002')
    index = child.expect(['reallyNeverExpectTHISSKIPTHISOUPUT', '.*router001:', '.*router002:', '.*router003:', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        #do_something('001')
        pass 
    elif index == 1:
        #do_something_else('002')
        do_something('002')
        pass
    elif index == 2:
        do_some_other_thing(child)
        child.sendline('show host name')
    elif index == 3:
        #do_something_completely_different('004')
        pass
    elif index == 4:
        #do_something_completely_different_differently(005')
        pass


chkBGPASN(child)
verifyDescR2(child)

addNIntAndRouting(child, promptR002)


exitDevice(child)
#exitDevice(child1)
#exitDevice(child3)





### Close out files
logFile.close()
