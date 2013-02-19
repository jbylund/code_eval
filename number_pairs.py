#!/usr/bin/python
import sys, math

def number_pairs(iarray,target):
    i = 0
    j = len(iarray) - 1
    num_solutions = 0
    ans = ""
    while(i < j):
        # if it's too small, then increment the smaller
        if(iarray[i] + iarray[j] < target):
            i += 1
        # if it's too large then decrement the greater
        elif(iarray[i] + iarray[j] > target):
            j -= 1
            if(j < 0):
                break
        else: # this is exact equality
            ans += `iarray[i]` + "," + `iarray[j]` + ";"
            # print target, " = ", iarray[i], " + ", iarray[j]
            i += 1
            j -= 1
            num_solutions += 1
            if(j < 0):
                break
    if(0 == len(ans)):
        print "NULL"
    else:
        print ans.rstrip(";")

test_cases = open(sys.argv[1], 'r')
lineslist = list()
n = 0
for test in test_cases:
    #print test
    target = int(test.split(";")[1])
    iarray = map(int,test.split(";")[0].split(","))
    number_pairs(iarray,target)


