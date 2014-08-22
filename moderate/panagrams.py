#!/usr/bin/python
import sys

def panagram(istring):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = list(alphabet)
    alphabet_set = set(alphabet_list)
    istring_list = list(istring)
    istring_set = set(istring_list)
    panagram = alphabet_set
    panagram = panagram - istring_set
    panagram_list = list(panagram)
    panagram_list.sort()
    panagram = "".join(panagram_list)
    if(0 == len(panagram)):
        print "NULL"
    else:
        print panagram

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    panagram(test.lower())

test_cases.close()
