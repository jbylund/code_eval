#!/usr/bin/python
import sys

# return the number of ways that
# inum elements of iarray can sum to target
def num_ways_to_decode(istring):
    if(0 == len(istring)):
        return 0
    if(1 == len(istring)):
        print "1 for " + `istring[0]`
        return 1

    if(len(istring) > 1):
        if(int(istring[0:1]) < 27):
            print "len(istring) = " + `len(istring)`
            print "istring = |" + istring + "|"
            print "2 for " + `istring[0:1]`
            return 2 + num_ways_to_decode(istring[1:]) + num_ways_to_decode(istring[2:])

    print "1 for " + `istring[0]`
    return 1 + num_ways_to_decode(istring[1:])

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print num_ways_to_decode(test)

test_cases.close()
