#!/usr/bin/python
import sys

def generate_m(a,b,c,r,k):
    m = list()
    m.append(a)
    for i in range(1,k):
        m.append((b * m[i - 1] + c) % r)
    return m

def get_nth_element(m,k,n):
    while(n > len(m)):
        possible_next_vals = set(range(0,k+1)) # non-negative integers
        possible_next_vals -= set(m[-k:]) # remove those which are already contained
        nextval = min(possible_next_vals) # the next val is the min of those not contained
        m.append(nextval) # append the next val
    return m[n-1]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = map(int,test.rstrip().split(","))
    n = test[0]
    k = test[1]
    a = test[2]
    b = test[3]
    c = test[4]
    r = test[5]
    m = generate_m(a,b,c,r,k)
    print get_nth_element(m,k,n)
test_cases.close()
