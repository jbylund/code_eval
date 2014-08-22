#!/usr/bin/python
import sys

def do_executions(n,m):
    people = range(n)
    order = "" # list()
    this_death = 0
    while(len(people)):
        this_death += m-1 # increment by one less than you might think because we're popping one
        this_death %= len(people)
        # order.append(people.pop(this_death))
        order += `people.pop(this_death)` + " "
    print order.rstrip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    n = int(test.split(",")[0])
    m = int(test.split(",")[1])
    do_executions(n,m)

test_cases.close()
