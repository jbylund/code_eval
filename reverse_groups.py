#!/usr/bin/python
import sys

def reverse_groups(iarray,n):
    for i in range(0,len(iarray)-n+1,n):
        chunk = iarray[i:i+n]
        iarray[i:i+n] = chunk[::-1]

    ans = ""
    for i in range(len(iarray)):
        ans += `iarray[i]` + ","
    ans = ans.rstrip(",")
    print ans
    

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    n = int(test.split(";")[1])
    iarray = map(int, test.split(";")[0].split(","))
    reverse_groups(iarray,n)

test_cases.close()
