#!/usr/bin/python
import sys

def trailing_string(a,b):
    if (a[-len(b):] == b):
        return 1
    return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    # 'test' represents the test case, do something with it
    print trailing_string(test.split(",")[0].strip(),test.split(",")[1].strip())

test_cases.close()
