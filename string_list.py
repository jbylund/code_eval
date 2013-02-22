#!/usr/bin/python
import sys,itertools

def list_permutations(length, letters):
    newletters = list(set(letters))
    newletters = newletters * length
    myperms = itertools.permutations(newletters,length)
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
    length = int(test.split(",")[0])
    letters = list(test.split(",")[1].rstrip())
#    print length, letters
    list_permutations(length, letters)
test_cases.close()
