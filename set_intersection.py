#!/usr/bin/python
import sys

# 5045616
def print_intersection(set1,set2):
    intersection = set1
    intersection &= set2
    print_list(sorted(list(intersection)))

def print_list(iarray):
    ans = ""
    for i in range(len(iarray)-1):
        iarray[i]=int(iarray[i])
        ans += `iarray[i]` + ','
    if(len(iarray) > 0):
        ans += `int(iarray[len(iarray)-1])`
    print ans


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    inputs = test.split(";")
    print_intersection(set(inputs[0].split(",")),set(inputs[1].split(",")))

test_cases.close()
