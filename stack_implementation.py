#!/usr/bin/python
import sys

class stack:
    def __init__(self):
        self.data = list()
        return

    def push(self,value):
        self.data.append(value)

    def pop(self):
        if (self.is_empty()):
            return ""
        return self.data.pop()

    def is_empty(self):
        return(0 == len(self.data))

def make_stack(ilist):
    mystack = stack()
    for i in range(len(ilist)):
        mystack.push(ilist[i])
    return mystack

def pop_every_other(mystack):
    ans = ""
    while(not mystack.is_empty()):
        ans += `mystack.pop()` + " "
        mystack.pop()

    print ans.rstrip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    mystack = make_stack(map(int,test.split()))
    pop_every_other(mystack)

test_cases.close()
