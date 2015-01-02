#!/usr/bin/python
import sys

def find_first_cycle(iarray):
    len_longest_repeated = 0
    longest_repeated = None
    for start in range(len(iarray)-1): # ((len(iarray)+1)//2):
        for i in range((len(iarray)-start)//2,0,-1):
            if(i <= len_longest_repeated):
                continue
            searcharray = iarray[start:start+i]
            if(0 == len("".join(searcharray).rstrip())):
                continue
            if(occurrences(iarray[start+i:],searcharray) > 0):
                longest_repeated = "".join(map(str,searcharray)).rstrip()
                len_longest_repeated = len(longest_repeated)
    if(None != longest_repeated):
        print longest_repeated
    else:
        print "NONE"

def occurrences(iarray, isubarray):
#    print "looking for |" + "".join(isubarray) + "|"
    for i in range(len(iarray)-len(isubarray)+1):
#        print "in |" + "".join(iarray[i:i+len(isubarray)]) + "|"
        if(isubarray == iarray[i:i+len(isubarray)]):
            return 1
    return 0

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
#    print test
    find_first_cycle(list(test))
test_cases.close()
