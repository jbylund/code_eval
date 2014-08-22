#!/usr/bin/python
import sys

# Brian Kernighan's method
def popcnt(inum):
    c = 0
    while(inum):
        inum &= inum - 1 # clear the least significant bit set
        c += 1
    return c

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print popcnt(int(test))

test_cases.close()
