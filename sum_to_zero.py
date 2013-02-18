#!/usr/bin/python
import sys

# return the number of ways that
# inum elements of iarray can sum to target
def num_ways_n_sum_to(inum, target, iarray):
    num_solns = 0
    if(1 == inum):
        num_solns = iarray.count(target)
    else:
        for i in range(len(iarray)):
            curr_val = iarray[i]
            num_solns += num_ways_n_sum_to(inum - 1, target - curr_val, iarray[i+1:len(iarray)])
#    print "f(" + `inum` + "," + `target` + "," + `iarray` + ") = " + `num_solns`
    return num_solns

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    test_array = map(int, test.split(","))
    num_solns = 0
    print num_ways_n_sum_to(4,0,test_array)

test_cases.close()
