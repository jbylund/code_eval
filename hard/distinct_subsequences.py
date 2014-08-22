#!/usr/bin/python
import sys,itertools

def count_subsequences(istring,isub):
#    print list(istring)
#    print list(isub)
    # iterate combinations, if the combination is the substring
    # then that's one
    distinct_substrings = 0
    indices = range(len(istring))
    mycombinations = itertools.combinations(indices,len(isub))
    for i in mycombinations:
        j = len(isub) - 1
        while(j >= 0):
            if(istring[i[j]] != isub[j]):
                break
            j -= 1

        # if you get to the bottom the strings are equivalent
        if(j < 0):
            distinct_substrings += 1
    return distinct_substrings

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    x = test.split(",")[0]
    z = test.split(",")[1]
    print count_subsequences(x,z)

test_cases.close()
