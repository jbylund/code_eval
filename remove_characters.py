#!/usr/bin/python
import sys

# remove all characters in b from a
def remove_characters(a, b):
    b = b.lstrip()
    return a.translate(None,b).lstrip().rstrip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    inputs = test.split(",")
    print remove_characters(inputs[0],inputs[1])

test_cases.close()
