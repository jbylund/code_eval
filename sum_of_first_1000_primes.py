#!/usr/bin/python
from math import sqrt, ceil
import sys

# return true if prime, otherwise false
def is_prime(num_to_test):
    # all primes are of the form 6k +- 1, with the exception of 2 and 3
    # this is because any integer n = (6k + i) for some integer k and i = -1, 0, 1, 2, 3, 4;
    # 2 divides (6k + 0), (6k + 2), (6k + 4);
    # and 3 divides (6k + 3)
    # test if n is divisible by 2 or 3
    if(2 == num_to_test):
        return True

    if(3 == num_to_test):
        return True

    if(0 == num_to_test % 2):
        return False

    if(0 == num_to_test % 3):
        return False

    # then check all d = 6k +- 1, d<=sqrt(n), 1/3 as many tests as testing all d
    k = 1
    while(6*k-1 <= sqrt(num_to_test)):
#        print "current k is " + `k`
#        print "testing divisors " + `6*k-1` + " and " + `6*k+1`
        d = 6*k - 1
        if(0 == num_to_test % d):
            return False
        d = 6*k + 1
        if(0 == num_to_test % d):
            return False
        k = k + 1

    if(1 == num_to_test): # by definition 1 is not prime
        return False

    return True

def sum_first_n_primes(n):
    num_primes = 0
    i = 0
    ans = 0
    while(num_primes < n):
        i = i + 1 # move on to the next number
        if(is_prime(i)):
            print i
            num_primes = num_primes + 1 # we caught a prime
            ans = ans + i            

    return ans

print sum_first_n_primes(1000)

sys.exit(0)
