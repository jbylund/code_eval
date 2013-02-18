#!/usr/bin/python
import sys

def is_rotation(a,b):
    a = a + a
    if(a.find(b) > 0):
        return True
    return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
    print is_rotation(test.split(",")[0],test.split(",")[1])

test_cases.close()
