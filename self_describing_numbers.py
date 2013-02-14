#!/usr/bin/python
import sys

# determine if inum is self describing
def is_self_describing(inum):
    pos = 0
    for pos in range(len(str(inum))):
        digit = int(str(inum)[pos])
        # print "digit = " + `digit`
        occurrences = num_occurrences_of_digit(inum,pos)
        # print "occurrences of " + `pos` + " = " + `occurrences`
        if(digit != occurrences):
            return False
    return True

# count the number of occurrences of digit in
# the base 10 rep of inum
def num_occurrences_of_digit(inum, digit):
    occurrences = 0
    while(inum > 0):
        if(digit == inum % 10):
            occurrences += 1
        inum //= 10
    return occurrences

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    if(is_self_describing(int(test))):
        print 1
    else:
        print 0

test_cases.close()
