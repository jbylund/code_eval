#!/usr/bin/python
import sys

class grid:
    def __init__(self):
        self.data = [0 for i in range(256*256)]

    def operate(self,iarray):
        if("QueryRow" == iarray[0]):
            print sum(self.data[int(iarray[1])*256:(1+int(iarray[1]))*256:1])
        if("QueryCol" == iarray[0]):
            print sum(self.data[int(iarray[1]):len(self.data):256])
        if("SetRow" == iarray[0]):
            for i in range(256*int(iarray[1]),256*(1+int(iarray[1]))):
                self.data[i] = int(iarray[2])
            return
        if("SetCol" == iarray[0]):
            for i in range(int(iarray[1]),len(self.data),256):
                self.data[i] = int(iarray[2])
            return

mygrid = grid()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test.rstrip())):
        continue
    mygrid.operate(test.split())

test_cases.close()
