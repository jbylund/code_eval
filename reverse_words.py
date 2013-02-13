#!/usr/bin/python
import sys

def reverse_words(line):
    print " ".join(line.split()[::-1])
    return



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    reverse_words(test)

test_cases.close()
