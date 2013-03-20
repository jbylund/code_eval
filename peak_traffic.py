#!/usr/bin/python
import sys,itertools

def make_connected_components(interactions):
    connected_components = list()
    connected_components.append(list())
    connected_components[0].append(0)
    # now interactions is an adjacency graph
    # print all connected components of at least 3 elements
    # if the graph containing i 
    for i in xrange(1,len(interactions)): # loop over users
        for j in xrange(len(connected_components)): # loop over components
            curr_component = connected_components[j]
            connected = True
            for k in curr_component:
                if(False == interactions[i][k]):
                    connected = False
                    break
            if(connected):
                # print i," is in the ", j, 'th component'
                curr_component.append(i) # put i in the current component
                break # break the loop over components
        if(False == connected):
            # print i," is not in a connected component"
            connected_components.append(list())
            connected_components[-1].append(i)
    return connected_components

def list_sub_components(connected_components):
    ans = list()
    for curr_component in connected_components:
        for i in xrange(3,1+len(curr_component)):
            ans.extend(itertools.combinations(curr_component,i))
    return ans

def make_clusters(sub_components,int2user):
    clusters = list()
    for i in sub_components:
        clusters.append(list())
        for j in i:
            clusters[-1].append(int2user[j])
        clusters[-1].sort()
    return clusters

def make_string_clusters(clusters):
    string_clusters = list()
    for i in clusters:
        string_clusters.append(", ".join(i))
    return sorted(string_clusters)


# make the list of users, and the user2int & int2user translations
users = set()
user2int = dict()
int2user = dict()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    u1 = test.split()[-2]
    u2 = test.split()[-1]
    if(u1 not in users):
        user2int[u1] = len(users)
        int2user[len(users)] = u1
        users.add(u1)
        pass
    if(u2 not in users):
        user2int[u2] = len(users)
        int2user[len(users)] = u2
        users.add(u2)
test_cases.close()

## initialize the interactions matrix
interactions = list()
for i in xrange(len(users)):
    col = [False for i in users]
    interactions.append(col)

## read in the interactions matrix
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    u1 = test.split()[-2]
    i1 = user2int[u1]
    u2 = test.split()[-1]
    i2 = user2int[u2]
    interactions[user2int[u1]][user2int[u2]] = True
test_cases.close()

## allow only bidirectional interactions
for i in xrange(len(users)):
    interactions[i][i] = True
    for j in xrange(i+1,len(users)):
        interactions[i][j] = (interactions[i][j] and interactions[j][i])
        interactions[j][i] = interactions[i][j]

connected_components = make_connected_components(interactions)
sufficiently_large_cc = list()
for i in connected_components:
    if(len(i) >= 3):
        sufficiently_large_cc.append(i)

connected_components = sufficiently_large_cc

sub_components = list_sub_components(connected_components)
clusters = make_clusters(sub_components,int2user)
string_clusters = make_string_clusters(clusters)

for i in string_clusters:
    print i

