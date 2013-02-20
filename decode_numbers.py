#!/usr/bin/python
import sys

class code_tree:
    def __init__(self,istring):
        self.left  = "0"
        self.right = "0"
        self.left_tree = -1
        self.right_tree = -1
        if(0 == len(istring)):
            return
        self.left  = istring[0]
        if(1 == len(istring)):
            return
        self.right      = istring[0:1+1]
        self.left_tree  = code_tree(istring[1:len(istring)])
        self.right_tree = code_tree(istring[2:len(istring)])

    def num_solutions(self):
        if(-1 == self.left_tree):
            return 1
        if((10 <= int(self.right)) and (int(self.right) < 27)):
            return self.left_tree.num_solutions() + self.right_tree.num_solutions()
        else:
            return self.left_tree.num_solutions()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    print code_tree(test).num_solutions()

test_cases.close()
