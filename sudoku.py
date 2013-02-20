#!/usr/bin/python
import sys

class sudoku:
    def __init__(self,size,data):
        self.size = size
        self.data = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                self.data[i][j] = data[i*size + j] - 1

    def is_valid(self):
        check_array = list()
        # check columns
        for i in range(self.size):
            check_array = list()
            for j in range(self.size):
                check_array.append(self.data[i][j])
            check_array.sort()
            if(check_array != range(self.size)):
                return False
        # check rows
        for j in range(self.size):
            check_array = list()
            for i in range(self.size):
                check_array.append(self.data[i][j])
            check_array.sort()
            if(check_array != range(self.size)):
                return False
        # determine the number of meta-rows        
        msize = 0
        while(msize**2 != self.size):
            msize += 1
        for mrow in range(msize):
            for mcol in range(msize):
                check_array = list()
                for row in range(msize):
                    for col in range(msize):
                        irow = mrow*msize+row
                        icol = mcol*msize+col
                        check_array.append(self.data[irow][icol])
                check_array.sort()
                if(check_array != range(self.size)):
                    print check_array
                    return False
        return True

def matrix_print(imat):
    for i in range(len(imat)):
        for j in range(len(imat[0])):
            sys.stdout.write(`imat[i][j]`+" ")
        print

test_cases = open(sys.argv[1], 'r').readlines()
i = 0
while(i < len(test_cases)):
    # ignore test if it is an empty line
    if(0 == len(test_cases[i])):
        i += 1
        continue
    test_cases[i] = test_cases[i].rstrip()
    size = int(test_cases[i].split(";")[0])
    grid = map(int,test_cases[i].split(";")[1].split(","))
    mysudoku = sudoku(size,grid)
    print mysudoku.is_valid()
    i += 1

