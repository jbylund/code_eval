#!/usr/bin/python
import sys

def sum_of_integers(iarray):
    max_sum = 0
    for start in range(0,len(iarray)): # this is the length of the sub arrays we're considering
        for end in range(start+1,len(iarray)+1):
            max_sum = max(max_sum,sum(iarray[start:end]))
    return max_sum

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    print sum_of_integers(map(int,test.split(",")))
test_cases.close()
