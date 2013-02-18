#!/usr/bin/python
import sys

def matrix_print(imat):
    for i in range(len(imat)):
        for j in range(len(imat[0])):
            sys.stdout.write(`imat[i][j]`+" ")
        print

def minimum_path(my_matrix):
    size = len(my_matrix)
    for j in range(size-2, -1, -1):
        my_matrix[size - 1][j] += my_matrix[size - 1][j+1]
        my_matrix[j][size - 1] += my_matrix[j+1][size - 1]

    for k in range(size-2, -1, -1):
        for j in range(size-2, -1, -1):
            my_matrix[k][j] += min(my_matrix[k + 1][j], my_matrix[k][j + 1])

    return my_matrix[0][0]

test_cases = open(sys.argv[1], 'r').readlines()
i = 0
while(i < len(test_cases)):
    # ignore test if it is an empty line
    if(0 == len(test_cases[i])):
        i += 1
        continue

    size = int(test_cases[i].rstrip())

    my_matrix = [[0 for j in range(size)] for k in range(size)]

    for j in range(size):
        i += 1
        this_row = map(int,test_cases[i].rstrip().split(","))
        for k in range(size):
            my_matrix[j][k] = this_row[k]

    print minimum_path(my_matrix)

    i += 1


