#!/usr/bin/python
import sys,string

def list_subtractions(iword):
    ans = list()
    for i in range(len(iword)):
        ans.append(iword[0:i] + iword[i+1:])
    return ans

def list_mutations(iword):
    ans = set()
    for pos in range(len(iword)):
        for target in range(len(string.ascii_lowercase)):
            mutation = iword[0:pos] + string.ascii_lowercase[target] + iword[pos+1:]
            ans.add(mutation)
    return ans

def list_additions(iword):
    ans = set()
    for pos in range(len(iword)+1):
        for target in range(len(string.ascii_lowercase)):
            addition = iword[0:pos] + string.ascii_lowercase[target] + iword[pos:]
            ans.add(addition)
    return ans

def network_size(iword,wordset):
    # initialize the list
    network = list()
    network_set = set()
    network.append(iword)
    network_set.add(iword)

    # iterate over every member of the set
    i = 0
    while(i < len(network)):
        current_word = network[i]
        # the things that neighbor this one are, subtractions, additions & mutations
        neighbors = list_subtractions(current_word)
        neighbors += list_additions(current_word)
        neighbors += list_mutations(current_word)
        for j in neighbors:
            if(j in network_set):
                continue
            if ( j in wordset ):
                network.append(j)
                network_set.add(j)
        i += 1

    # if the seed word is not a real word
    if(not(iword in wordset)):
        network_set.remove(iword)
    return len(network_set)

# process the input
wordset = set()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    wordset.add(test.rstrip())
test_cases.close()

print network_size("hello",wordset)
