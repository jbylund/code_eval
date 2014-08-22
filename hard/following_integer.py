#!/usr/bin/python
import sys

# find the next integer with the same number
# of each digit from 1-9 (any number of zeros)
def get_next_integer(inum):
    str_rep = str(inum)
    list_rep = map(int,list(str_rep))
    list_rep_rev = sorted(list_rep)
    list_rep_rev.reverse()

    if(list_rep == list_rep_rev):
        ans = list_rep
        ans.append(0)
        ans.sort()
        i = 1 # start at 1 because we know there is a zero
        while(0 == ans[i]):
            i += 1
        ans[0] = ans[i]
        ans[i] = 0
        return intlist2int(ans)
    else:
        i = len(list_rep) - 1
        while(list_rep[i-1] >= list_rep[i]):
            i -= 1
        left = i - 1
        # sort everything to the right of the left swap
        list_rep[i:] = sorted(list_rep[i:])
        right = i
        while(list_rep[right] <= list_rep[left]):
            right += 1
        temp = list_rep[left]
        list_rep[left] = list_rep[right]
        list_rep[right] = temp
        list_rep[right:] = sorted(list_rep[right:])
        return intlist2int(list_rep)

def intlist2int(intlist):
    intlist = map(str,intlist)
    return int("".join(intlist))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    print get_next_integer(int(test))

test_cases.close()
