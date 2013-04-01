#!/usr/bin/python
import sys,itertools,math

def get_distance(location_a,location_b):
    dx = location_a[0] - location_b[0]
    dy = location_a[1] - location_b[1]
    return math.sqrt(dx*dx + dy*dy)

def make_distance_matrix(locations):
    distance_matrix = list()
    for i in locations:
        distance_matrix.append([0 for i in locations])
    for i in xrange(len(locations)):
        for j in xrange(i+1,len(locations)):
            distance_matrix[i][j] = get_distance(locations[i],locations[j])
            distance_matrix[j][i] = distance_matrix[i][j]
    return distance_matrix

def get_best_path(locations):
    distance_matrix = make_distance_matrix(locations)

    best_dist = 2*sum(distance_matrix[0])
    for i in itertools.permutations(xrange(len(locations))):
        if(i[0] != 0):
            break
        route = 0
        for stop_num in xrange(len(i)-1):
            route += distance_matrix[i[stop_num]][i[stop_num + 1]]
        if(route < best_dist):
            best_route = list(i)
            best_dist = route
    for i in xrange(len(best_route)):
        best_route[i] += 1
    return best_route

locations = list()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    locations.append(map(float,test.split("(")[1].rstrip(")").split(",")))
test_cases.close()

best_path = get_best_path(locations)

for i in best_path:
    print i
