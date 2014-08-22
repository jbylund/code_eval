#!/usr/bin/python
import sys

def matrix_print(imat):
    for i in range(len(imat)):
        for j in range(len(imat[0])):
            sys.stdout.write(`imat[i][j]`+" ")
        print

def increment_neighbors(irow,icol,imat):
    lrow = max(0,irow-1)
    mrow = min(len(imat)-1, irow+1)
    lcol = max(0,icol-1)
    mcol = min(len(imat[0])-1, icol+1)
    for i in range(lrow,mrow+1):
        for j in range(lcol,mcol+1):
            imat[i][j] += 1
    return imat

def minesweeper(rows,cols,bombs):
    mylist = [0] * rows * cols
    mymatrix = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(len(bombs)):
        if("*" == bombs[i]):
            mylist[i] = 1
            row = i // cols
            col = i % cols
            mymatrix[row][col] = 1


    ans = [[0 for i in range(cols)] for j in range(rows)]

    for irow in range(rows):
        for icol in range(cols):
            if(1 == mymatrix[irow][icol]):
                ans = increment_neighbors(irow,icol,ans)
    ans_str = ""
    for i in range(len(bombs)):
        if("*" == bombs[i]):
            ans_str += "*"
        else:
            row = i // cols
            col = i % cols
            ans_str += `int(ans[row][col])`
    print ans_str

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    # 'test' represents the test case, do something with it
    test = test.rstrip()
    rows = int(test.split(";")[0].split(",")[0])
    cols = int(test.split(";")[0].split(",")[1])
    bombs = test.split(";")[1]
    minesweeper(rows,cols,bombs)

test_cases.close()
