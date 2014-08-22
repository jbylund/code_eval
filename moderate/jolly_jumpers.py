#!/usr/bin/python

#Sample code to read in test cases:

import sys

def is_jolly(istring):
    sequence = istring.split()
    seq_len = int(sequence.pop(0))
    s = set()
    # accumulate the abs of differences
    for i in range(1,len(sequence)):
        s.add(abs(int(sequence[i])-int(sequence[i-1])))
    # if there are not the correct number of differences
    if(len(s) != (seq_len - 1)):
        return False
    # if it does not start at 1 it doesn't work
    if(min(s) != 1):
        return False
    # it is jolly if the max is seq_len-1
    return ((seq_len - 1) == max(s))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue

    if(is_jolly(test)):
        print "Jolly"
    else:
        print "Not jolly"

test_cases.close()
