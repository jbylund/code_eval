#!/usr/bin/python
import sys

# A robot is located at the top-left corner of a 4x4 grid. 
# The robot can move either up, down, left, or right, 
# but can not visit the same spot twice. 
# The robot is trying to reach the bottom-right corner of the grid. 

def solutions_from(x,y,visited):
    if(max(x,y) >= size):
        return 0 # out of bounds
    if(min(x,y) < 0):
        return 0 # out of bounds
    if((x,y) in visited):
        return 0 # this is a path crossing which is illegal, so no solutions
    else:
        visited.add((x,y)) # add the one where we currently are
        if((x,y) == (size-1,size-1)):
            paths = 1 # there is exactly this way to get here since you can't leave and come back
        else:
            paths = (solutions_from(x+1,y,visited)
                   + solutions_from(x-1,y,visited)
                   + solutions_from(x,y+1,visited)
                   + solutions_from(x,y-1,visited))
            # the number of solutions using the current path is the
            # number using the path and this square from any of the 4 directions
        visited.remove((x,y)) # add the one where we currently are, so other paths can use it later
        return paths # return the number of solutions from here

size = 4 # the grid is 4x4
visited = set()
print solutions_from(0,0,visited) # print the number of solutions starting from (0,0) with no other squares visited
