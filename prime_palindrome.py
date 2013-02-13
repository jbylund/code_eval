#!/usr/bin/python
from math import sqrt, ceil
import sys

# return true if palindrome, otherwise false
def is_palindrome(num_to_test):
    stringval = `num_to_test`
    reverse_stringval = stringval[::-1]
    if(stringval == reverse_stringval):
        return True
    return False

# return true if prime, otherwise false
def is_prime(num_to_test):
    # all primes are of the form 6k +- 1, with the exception of 2 and 3
    # this is because any integer n = (6k + i) for some integer k and i = -1, 0, 1, 2, 3, 4;
    # 2 divides (6k + 0), (6k + 2), (6k + 4);
    # and 3 divides (6k + 3)
    # test if n is divisible by 2 or 3
    if(0 == num_to_test % 2):
        return False
    if(0 == num_to_test % 3):
        return False
    # then check all d = 6k +- 1, d<=sqrt(n), 1/3 as many tests as testing all d
    for k in range(1,int(ceil((sqrt(num_to_test)+1)/6)),1):
        #print "current k is " + `k`
        # print "testing divisors " + `6*k-1` + " and " + `6*k+1`
        d = 6*k - 1
        if(0 == num_to_test % d):
            return False
        d = 6*k + 1
        if(0 == num_to_test % d):
            return False
    return True

for i in range(1000,1,-1):
    if(not is_palindrome(i)):
        continue
    if(is_prime(i)):
        print i
        sys.exit(0)

sys.exit(1)
