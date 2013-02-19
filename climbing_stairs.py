#!/usr/bin/python
import sys
from math import factorial

def count_paths(num_stairs):
    num_paths = 0
    onesteps = num_stairs
    twosteps = 0
    while(onesteps >= 0):
        num_paths += num_permutations(onesteps, twosteps)
        twosteps += 1
        onesteps = num_stairs - (2 * twosteps)
    return num_paths

def num_permutations(onesteps, twosteps):
    return factorial(onesteps+twosteps)/(factorial(onesteps)*factorial(twosteps))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    print count_paths(int(test))   

test_cases.close()
