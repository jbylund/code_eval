#!/usr/bin/python
import sys

def array_absurdity(test):
    n = int(test.split(";")[0])
    seen = [False for i in range(n-1)]
    seq = test.split(";")[1].split(",")
    for i in range(len(seq)):
        a = int(seq[i])
        if(seen[a]):
            return a
        seen[a] = True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print array_absurdity(test)

test_cases.close()
