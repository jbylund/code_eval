#!/usr/bin/python
import sys, collections
# First I decided against solving for a grid which contains all 
# possible accessible squares & then solving iteratively because I 
# figured it would add unnecessary complexity.
# Second I decided to use a breadth-first search instead of a recursive 
# depth first search to limit recursion depth.
# and since I decided on a BFS a deque seemed the logical structure to 
# use.
# I put the visited squares in a set so I can quickly check if I've 
# already walked them, and it has the nice side benefit that I can just
# look at how many are in the set at the end to see how many I visited.
# The final simplification I made was only considering the first 
# quadrant & then adding the mirrored squares to the visited set 
# (because the set of accessible points has two planes of symmetry
# (because everything revolves around absolute values))

# get the sum of digits of a number
def sum_digits(inum):
    inum = abs(inum)
    ans = 0
    while(inum > 0):
        ans += inum % 10
        inum //= 10
    return ans

# this represents a square of my grid
class square:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # two grid squares are equal iff x1=x2 and y1=y2
    def __eq__(self,other):
        if(self.x != other.x):
            return False
        return (self.y == other.y)

    def __hash__(self):
        return 127 * self.x + self.y

    def __repr__(self):
        return "square at ( " + `self.x` + ", " + `self.y` + ")"

    def is_accessible(self):
        # I'm restricting my search to the first quadrant, knowing the other quadrants will be symmetric
        if(self.x < 0):
            return False
        if(self.y < 0):
            return False
        sum_digits_abs_x = sum_digits(abs(self.x))
        sum_digits_abs_y = sum_digits(abs(self.y))
        if((sum_digits_abs_x + sum_digits_abs_y) <= 19):
            return True
        return False

    def explore(self,already_walked,queue):
        if(not self.is_accessible()):
            return
        if(self in already_walked):
            return

        already_walked.add(self)

        # now add the symmetry squares
        already_walked.add(square(-1*self.x,self.y)) # included because of symmetry
        already_walked.add(square(self.x,-1*self.y)) # included because of symmetry
        already_walked.add(square(-1*self.x,-1*self.y)) # included because of symmetry

        neighbors = self.list_neighbors()
        for i in neighbors:
            queue.append(i)

    def list_neighbors(self):
        ans = list()
        ans.append(square(self.x+1,self.y))
        ans.append(square(self.x,self.y+1))
        # assume x,y is accessible (for x,y > 0, others follow from symmetry)
        # then while x != 0 (mod 10), x-1,y is accessible, 
        # extending we have if (x,y) is accessible then (x-(x%10),y-(y%10))
        # is accessible, which means, that if (10a,10b) is not accessible then
        # (10a+x,10b+y) is not accessible for any x < 10, y < 10
        # since digit_sum(10a+x) = digit_sum(a) + digit_sum(x)
        # which means that it is enough to check only in the positive direction
        # not needed because every accessible square has an accessible parent
        # in either the -x or -y direction
        # this saves us a fair bit of time
        # ans.append(square(self.x-1,self.y)) 
        # ans.append(square(self.x,self.y-1))
        return ans

queue = collections.deque() # this is my queue for squares to explore
already_walked = set() # this is the cumulative set of squares I have explored
queue.append(square(0,0)) # this is the first square I'm going to explore
while(len(queue) > 0): # while I might be able to explore more
    queue.popleft().explore(already_walked,queue) # explore the first item in the queue, adding its neighbors to the end of the queue

print len(already_walked) # this is the total number of squares that were accessible
