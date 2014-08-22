#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
triangle = list()
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    triangle.append(map(int,test.split()))
test_cases.close()

# because I think counting up is "nicer" than counting down
# I'm going to flip the whole triangle upside down and
# then count up
triangle = triangle[::-1]

# start at the 1'st (not zero'th row, because the zero'th row is already done)
for row in xrange(1,len(triangle)):
    # loop over the positions in the current row
    for j in xrange(len(triangle[row])):
        # and the most we could get from here to the end is
        # the current space + the most that we might have gotten 
        # from either the right or left paths
        triangle[row][j] = triangle[row][j] + max(triangle[row-1][j],triangle[row-1][j+1])

# finally the most that you could get from the whole
# shebang is left in the "top" space (which I put on the bottom)
print triangle[len(triangle)-1][0]
