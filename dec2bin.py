#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    print bin(int(test)).lstrip('0b')

test_cases.close()
