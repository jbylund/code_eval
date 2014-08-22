#!/usr/bin/python
import sys
import math

class point:
    def __init__(self,ilist):
        self.cords = ilist

def maxfloat(guess = 1.0):
        while(guess * 2 != guess):
            guess = guess * 2
        return guess

def find_min_distance(points_array):
    min_sq_dist = maxfloat()

    for i in range(len(points_array)):
        for j in range(i+1,len(points_array)):
            min_sq_dist = min(min_sq_dist,sq_dist(points_array[i],points_array[j]))

#    print "best found = ", math.sqrt(min_sq_dist)
    min_distance = math.sqrt(min_sq_dist)
#    print min_distance
    if(min_distance > 10000):
        return "INFINITY"
    else:
        return '{0:.4f}'.format(min_distance)

def sq_dist(ipoint,jpoint):
    sq_dist = 0
    for i in range(len(ipoint.cords)):
        sq_dist += (ipoint.cords[i]-jpoint.cords[i])**2
#        print sq_dist
#    print sq_dist
#    print
    return sq_dist

mypoints = list()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    if(1 == len(test.split())):
        if(0 < len(mypoints)):
            print find_min_distance(mypoints)
        mypoints = list()
    else:
        mypoints.append(point(map(int,test.split())))

test_cases.close()
