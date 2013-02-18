#!/usr/bin/python
import sys

# find the next integer with the same number
# of each digit from 1-9 (any number of zeros)
def get_next_integer(inum):
    print inum
    str_rep = str(inum)
    list_rep = map(int,list(str_rep))

    i = len(list_rep) - 1
    while((i-1 >= 0) and (list_rep[i-1] >= list_rep[i])):
        i -= 1

    if( 0 == i ):
        print "perfectly reversed"
        list_rep.sort()
        ans = list()
        ans.append(list_rep[0])
        ans.append(0)
        ans += list_rep[1:]
        print ans
        return intlist2int(ans)
    else:
        # want index of smallest number in 
        # list_rep[i:] which is greater than
        a = list_rep[i-1]
        shuffled_part = sorted(list_rep[i-1:])
        swap_index = shuffled_part.index(a) + 1
        a = shuffled_part.pop(swap_index)
        return intlist2int(list_rep[:i-1] + [a] + shuffled_part)

def intlist2int(intlist):
    intlist = map(str,intlist)
    print intlist
    return int("".join(intlist))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
    print get_next_integer(int(test))

test_cases.close()
