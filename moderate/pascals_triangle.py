#!/usr/bin/python
import sys

# return the number of ways that
# inum elements of iarray can sum to target
def do_pascal(depth, last_row):
    for i in range(len(last_row)):
        sys.stdout.write(`last_row[i]` + " ")
    if(0 == depth):
        print ""
        return
    last_row = [0] + last_row + [0]
    this_row = list()
    for i in range(len(last_row)-1):
        this_row.append(last_row[i] + last_row[i+1])
    do_pascal(depth - 1, this_row)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    do_pascal(int(test)-1,list([1]))

test_cases.close()
