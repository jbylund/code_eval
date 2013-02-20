#!/usr/bin/python
import sys

class code_tree:
    def __init__(self, parent):
        self.parent = parent
        self.value = None
        self.left_tree = None
        self.right_tree = None

    def push(self,inum):
        if(None == self.left_tree):
            self.value = inum
            self.left_tree = code_tree(self)
            self.right_tree = code_tree(self)
        else:
            if(inum < self.value):
                self.left_tree.push(inum)
            else:
                self.right_tree.push(inum)

    # find the last common ancestor of a & b
    def find_lca(self,a,b):
        if((a < self.value) and (b < self.value)):
            return self.left_tree.find_lca(a,b)
        if((a > self.value) and (b > self.value)):
            return self.right_tree.find_lca(a,b)
        return self.value

    def num_solutions(self):
        if(None == self.left_tree):
            return 1
        else:
            return 0

    def parent(self):
        return self.parent

# build up the tree
mytree = code_tree(None)
mytree.push(30)
mytree.push(8)
mytree.push(52)
mytree.push(3)
mytree.push(20)
mytree.push(10)
mytree.push(29)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    print mytree.find_lca(int(test.split()[0]), int(test.split()[1]))

test_cases.close()
