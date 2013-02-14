#!/usr/bin/python

#Sample code to read in test cases:

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue

    # 'test' represents the test case, do something with it

test_cases.close()
