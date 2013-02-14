#!/usr/bin/python
import sys

def rightmost_char(istring,ichar):
    print istring.find(ichar)
    return



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    inputs = test.split(",")
    rightmost_char(inputs[0],inputs[1])

test_cases.close()
