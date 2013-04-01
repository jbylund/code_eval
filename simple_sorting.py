#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    print " ".join(["%.3f" % f for f in sorted(map(float,test.split()))])
test_cases.close()
