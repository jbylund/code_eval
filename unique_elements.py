#!/usr/bin/python
import sys

def uniquify(iarray):
    iarray = sorted(list(set(iarray)))
    ans = ""
    for i in range(len(iarray)-1):
        iarray[i]=int(iarray[i])
        ans += `iarray[i]` + ','
    ans += `int(iarray[len(iarray)-1])`
    print ans


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    test = test.split(",")
    uniquify(test)

test_cases.close()
