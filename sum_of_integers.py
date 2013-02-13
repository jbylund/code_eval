#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
ans = 0
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    ans += int(test)

print ans
test_cases.close()
