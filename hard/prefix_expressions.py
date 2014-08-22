#!/usr/bin/python
import sys

class prefix_expression:
    def __init__(self,iarray):
        self.thisnode = iarray.pop()
        self.left     = None
        self.right    = None
        if(self.thisnode.isdigit()):
            return
        self.left  = prefix_expression(iarray)
        self.right = prefix_expression(iarray)
        return

    def value(self):
        if(self.thisnode.isdigit()):
            return int(self.thisnode)
        left  = self.left.value()
        right = self.right.value()
        if("+" == self.thisnode):
            return left + right
        if("*" == self.thisnode):
            return left * right
        if("/" == self.thisnode):
            return left / right


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    print test.rstrip()
    iarray = test.rstrip().split()
    irev = iarray
    irev.reverse()
    print prefix_expression(irev).value()
test_cases.close()
