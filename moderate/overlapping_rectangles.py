#!/usr/bin/python
import sys
def rectangles_overlap(coords):
    # first entirely to left of second
    if(coords[2] < coords[4]): 
        return False
    # second entirely to left of first
    if(coords[6] < coords[0]):
        return False
    # first entirely below second
    if(coords[1] < coords[7]):
        return False
    # second entirely below first
    if(coords[5] < coords[3]):
        return False
    return True


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    coords = map(int, test.split(","))
    print rectangles_overlap(coords)

test_cases.close()
