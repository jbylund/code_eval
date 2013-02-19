#!/usr/bin/python
import sys

class hand_of_change:
    def __init__(self,ones,threes,fives):
        self.ones   = ones
        self.threes = threes
        self.fives  = fives

    def num_coins(self):
        return self.ones + self.threes + self.fives

    def value(self):
        return self.ones + 3 * self.threes + 5 * self.fives

    def __repr__(self):
        ans = `self.value()` + " = "
        if(self.fives > 0):
            ans += `self.fives` + " fives,"
        if(self.threes > 0):
            ans += `self.threes` + " threes,"
        if(self.ones > 0):
            ans += `self.ones` + " ones,"

def list_hands_up_to(max_value):
    return list()

values = list()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    values.append(int(test))
test_cases.close()

print values
max_value = max(values)
hands = list_hands_up_to(max_value)

