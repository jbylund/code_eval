#!/usr/bin/python
import sys
import numpy as np

# 5045616
def primes_less_than(ival):
    # need to include 2, 3, then everything follows (6n+-1)
    num_to_precompute = 10000
    known_primes_list = list(sundaram3(num_to_precompute))
    known_primes_list.sort()

    possible_primes = set(known_primes_list)
    # now append 6 n+- 1 for
    i = num_to_precompute//6 + 1
    possible_primes.update(range(6*i+5,ival,6)) # 6n - 1
    possible_primes.update(range(6*i+7,ival,6)) # 6n - 1

    for i in range(2,len(known_primes_list)):
        n = known_primes_list[i]
        possible_primes.difference_update(range(n**2,ival,n))

    possible_primes_list = list(possible_primes)
    possible_primes_list.sort()

    start_index = 0
    while(possible_primes_list[start_index] <= max(known_primes_list)):
        start_index += 1

    for i in range(start_index,len(possible_primes_list)):
        n = possible_primes_list[i]
        if(n**2 > ival):
            break
        possible_primes.difference_update(range(n**2,ival,n))
    possible_primes_list = list(possible_primes)
    possible_primes_list.sort()
    return possible_primes_list

# 3231844
def myprime(n):
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom # floor division
    while (bottom*bottom<=n): # while square < n
        while (bottom<=top):
            if s[top]: # if top is a prime
                s[top*bottom] = 0 
            top -= 1
        bottom += 1
        while s[bottom]==0: # advance to the next possible prime
            bottom+=1
        top=n//bottom
    return [x for x in s if x]

def sundaram3(max_n):
    numbers = range(3, max_n + 1, 2)
    half = max_n // 2
    initial = 4

    for step in xrange(3, max_n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

    if initial > half:
        return [2] + filter(None, numbers)

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    # primes = primes_less_than(int(test))
    # primes = myprime(int(test))
    # primes = sundaram3(int(test))
    # primes = rwh_primes2(int(test))
    primes = primesfrom2to(int(test))
    print `len(primes)` + " primes less than " + `int(test)`

test_cases.close()
