#!/usr/bin/python
import sys,re

def is_sub(istring,pattern):
    pattern = pattern.replace("\*","%")
    pattern = pattern.replace("*",".*")
    pattern = pattern.replace("%","\*")
    if(None == re.search(pattern, istring)):
        return "false"
    return "true"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
    istring = test.split(",")[0]
    pattern = test.split(",")[1]
    print is_sub(istring,pattern)

test_cases.close()
