#!/usr/bin/python
import sys

def maximal_alignment(s1,s2):
    # remove characters from s1 not present in s2 (they don't align)
    s2contains = set(list(s2))
    s1 = filter(lambda x: (x in s2contains), s1)

    # remove characters from s2 not present in s1 (they don't align)
    s1contains = set(list(s1))
    s2 = filter(lambda x: (x in s1contains), s2)

    imatrix = list()
    for i in s2:
        imatrix.append([0 for j in s1])

    for i in xrange(len(s1)):
        imatrix[0][i] = int(s1[i] == s2[0])

    for i in xrange(len(s2)):
        imatrix[i][0] = int(s2[i] == s1[0])

    for i in xrange(1,len(s2)):
        for j in xrange(1,len(s1)):
            imatrix[i][j] = max(imatrix[i-1][j],imatrix[i][j-1],imatrix[i-1][j-1]+int(s1[j] == s2[i]))

    return get_alignment(s1,imatrix)

# given a scoring matrix, return the alignment
def get_alignment(s1,imatrix):
    ans = ""
    irow = len(imatrix) - 1
    icol = len(imatrix[0]) - 1
    while(irow >= 0 and icol >= 0 and imatrix[irow][icol] > 0):
        this_val = imatrix[irow][icol]
        if(irow > 0 and imatrix[irow-1][icol] == this_val):
            irow -= 1
        elif(icol > 0 and imatrix[irow][icol-1] == this_val):
            icol -= 1
        else:
            ans = s1[icol] + ans
            icol -= 1
            irow -= 1
    return ans

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    s1 = test.split(";")[0]
    s2 = test.split(";")[1]
    print maximal_alignment(s1,s2)
test_cases.close()
