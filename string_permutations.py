#!/usr/bin/python
import sys,itertools

def list_permutations(length, letters):
    myperms = itertools.permutations(letters,length)
    mystringperms = list()
    for i in myperms:
        mystringperms.append("".join(i))
    mystringperms = sorted(list(set(mystringperms)))
    print ",".join(mystringperms)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    letters = list(test.rstrip())
#    print length, letters
    list_permutations(len(letters), letters)
test_cases.close()
