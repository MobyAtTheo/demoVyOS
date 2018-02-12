#!/usr/bin/env python3


import pexpect

child = pexpect.spawn('ssh -l vyos 172.16.115.32')
child.expect ('.*assword:')
child.sendline ('vyatta')


child.expect(



def do_something(value):
    print('I\'m doing something.', value)


def chkBGPASN(child):
    child.expect('.*router002')
    index = child.expect (['reallyNeverExpectTHISSKIPTHISOUPUT', '.*router001:', '.*router002:', '.*router003:', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        #do_something('001')
    elif index == 1:
        #do_something_else('002')
    elif index == 2:
        #do_some_other_thing('003')
    elif index == 3:
        #do_something_completely_different('004')
    elif index == 4:
        #do_something_completely_different_differently(005')

child.interact()



