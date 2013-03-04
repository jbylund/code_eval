#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # if the line is empty do nothing
    if(0 == len(test.rstrip())):
        continue
    # split the line up into pieces
    marray = test.split()

    # if the length is less than 2 it can't possibly have
    # both contents and a number
    if(len(marray) < 2):
        continue

    # strip the index off the end
    mindex = int(marray.pop())

    # if the array is too short, do nothing
    if(mindex > len(marray)):
        continue
    else:
        # otherwise print that element
        print marray[-1*mindex]

test_cases.close()
