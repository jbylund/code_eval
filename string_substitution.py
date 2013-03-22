#!/usr/bin/python
import sys

def do_replacements(istring,replacements):
    ilist = list(istring)
    fixed = [False for i in ilist]
    for i in xrange(0,len(replacements),2):
        replace_a_b_string_fixed(list(replacements[i]),list(replacements[i+1]),ilist,fixed)
    return "".join(ilist)

def replace_a_b_string_fixed(a,b,ilist,fixed):
    i = 0
    while i + len(a) <= len(ilist):
        if(any(fixed[i:i+len(a)])):
            i += 1
            continue
        if(ilist[i:i+len(a)] == a):
            for j in xrange(0,len(a)):
                ilist.pop(i)
                fixed.pop(i)
            for j in xrange(0,len(b)):
                ilist.insert(i+j, b[j])
                fixed.insert(i+j, True)
        i += 1

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    istring = test.split(";")[0]
    replacements = test.split(";")[1].split(",")
    print do_replacements(istring,replacements)
test_cases.close()
