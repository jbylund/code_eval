#!/usr/bin/python
import sys

# determine if inum is happy
def is_self_describing(inum):
    return True

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    if(is_self_describing(int(test))):
        print 1
    else:
        print 0

test_cases.close()
