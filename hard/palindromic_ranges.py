#!/usr/bin/python
import sys

# return true if palindrome, otherwise false
def is_palindrome(num_to_test):
    stringval = `num_to_test`
    reverse_stringval = stringval[::-1]
    if(stringval == reverse_stringval):
        return True
    return False

def count_palindromic_ranges(lbound, ubound):
    irange = range(lbound,ubound+1)
    palindromes = [False] * len(irange)
    for i in range(len(irange)):
        palindromes[i] = is_palindrome(irange[i])

    interesting_ranges = 0
    for ilow in range(len(palindromes)):
        for ihi in range(ilow,len(palindromes)):
            # print irange[ilow], irange[ihi]
            if(0 == palindromes[ilow:ihi+1].count(True) % 2):
                interesting_ranges += 1
    return interesting_ranges

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
    print count_palindromic_ranges(int(test.split()[0]),int(test.split()[1]))
test_cases.close()
