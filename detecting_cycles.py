#!/usr/bin/python
import sys

def find_first_cycle(ilist):
    print ilist
    return

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    print find_first_cycle(test.split(" "))

test_cases.close()
