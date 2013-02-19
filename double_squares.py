#!/usr/bin/python
import sys, math

def count_double_sqaures(squares_array,inum):
    # print "inum  = ", inum
    i = 0
    # j = min(len(squares_array)-1,int(math.sqrt(inum)+1))
    j = len(squares_array) - 1

    num_solutions = 0
    while(i <= j):
        # if it's too small, then increment the smaller
        if(squares_array[i] + squares_array[j] < inum):
            i += 1
        # if it's too large then decrement the greater
        elif(squares_array[i] + squares_array[j] > inum):
            j -= 1
            if(j < 0):
                break
        else: # this is exact equality
            # print inum, " = ", squares_array[i], " + ", squares_array[j]
            i += 1
            j -= 1
            num_solutions += 1
            if(j < 0):
                break
    return num_solutions

test_cases = open(sys.argv[1], 'r')
lineslist = list()
n = 0
for test in test_cases:
    if(0 == n):
        n = int(test)
    else:
        lineslist.append(int(test.rstrip()))

perfect_squares = list()
i = 0
while(i**2 <= max(lineslist)):
    perfect_squares.append(i**2)
    i += 1

for i in range(len(lineslist)):
    print count_double_sqaures(perfect_squares,lineslist[i])

