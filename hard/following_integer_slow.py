#!/usr/bin/python
import sys

# find the next integer with the same number
# of each digit from 1-9 (any number of zeros)
def get_next_integer(inum):
    str_rep = str(inum)
    list_rep = map(int,list(str_rep))
    list_rep = filter (lambda a: a != 0, list_rep)
    list_rep.sort()
    inum = inum + 1
    while(sorted(list(str(inum))) != list_rep):
        ans_str = str(inum)
        ans_list = map(int,list(ans_str))
        ans_list = filter (lambda a: a != 0, ans_list)
        ans_list.sort()
        if(ans_list == list_rep):
            break
        inum = inum + 1
    return inum

def intlist2int(intlist):
    intlist = map(str,intlist)
    # print intlist
    return int("".join(intlist))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    test = test.rstrip()
#    print int(test), " => ", get_next_integer(int(test))
    print get_next_integer(int(test))

test_cases.close()
