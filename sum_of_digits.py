#!/usr/bin/python
import sys

def sum_of_digits(ival):
    ans = 0
    while(ival > 0):
        ans += (ival % 10)
        ival = int(ival/10)
    return ans

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print sum_of_digits(int(test))

test_cases.close()
