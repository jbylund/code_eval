#!/usr/bin/python
import sys

def play_fizz_buzz(fizznum, buzznum, maxnum):
    i = 1
    ans = ""
    while(i <= maxnum):
        if((0 == i % fizznum) and (0 == i % buzznum)):
            ans += "FB"
        elif(0 == i % fizznum):
            ans += "F"
        elif(0 == i % buzznum):
            ans += "B"
        else:
            ans += `i`
        i += 1
        ans += " "
    print ans.rstrip()
    return



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    inputs = test.split()
    play_fizz_buzz(int(inputs[0]),int(inputs[1]),int(inputs[2]))

test_cases.close()
