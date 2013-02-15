#!/usr/bin/python
import sys

# Integer N is Armstrong number
# if N = the sum of the n'th powers of its digits
def is_armstrong(inum):
    inum_orig = inum
    power = len(str(inum))
    armstrong = 0
    while(inum > 0):
        armstrong += (inum % 10)**power
        inum //= 10
    return (armstrong == inum_orig)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    print(is_armstrong(int(test)))

test_cases.close()
