#!/usr/bin/python
import sys

# determine if inum is happy
def is_happy(inum):
    s = set() # start with the empty set
    while((inum != 1) and (inum not in s)): # while we are neither 1 nor in a cycle
        s.add(inum) # add inum to the set
        inum = sum_square_of_digits(inum) # replace the number with the sum of the squares of its digits
    return (1 == inum)

def sum_square_of_digits(inum):
    ans = 0 # our accumulator
    while(inum > 0):
        ans += (inum % 10)**2 # add the square of the 1's place
        inum //= 10 # right shift the number (in 10 speak)
    return ans

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    if(is_happy(int(test))):
        print 1
    else:
        print 0

test_cases.close()
