#!/usr/bin/python
import sys

def a_mod_b(a, b):
    return (a - ((a//b)*b))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    inputs = test.split(",")
    a = int(inputs[0])
    b = int(inputs[1])
    print a_mod_b(a,b)

test_cases.close()
