#!/usr/bin/python
import sys
# should probably be done with dynamic programming
# but in the interest of expediency

# find the first 
def find_first_cycle(iarray):
    for start in range(len(iarray)-1): # ((len(iarray)+1)//2):
        for i in range((len(iarray)-start)//2,0,-1):
            searcharray = iarray[start:start+i]
            myo = occurrences(iarray[start+i:],searcharray)
            if(myo > 0):
                print " ".join(map(str,searcharray)).rstrip()
                return

def occurrences(iarray, isubarray):
    for i in range(len(iarray)-len(isubarray)+1):
        if(isubarray == iarray[i:i+len(isubarray)]):
            return 1
    return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    find_first_cycle(map(int,test.split()))

test_cases.close()
