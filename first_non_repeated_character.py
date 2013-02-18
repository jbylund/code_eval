#!/usr/bin/python
import sys

def first_non_repeated(test):
    pos = 0
    while(test.count(test[pos]) > 1):
        pos += 1
    if(pos < len(test)):
        return test[pos]
    else:
        return None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print first_non_repeated(test)

test_cases.close()
