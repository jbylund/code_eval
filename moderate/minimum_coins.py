#!/usr/bin/python
import sys

def min_coins_equaling(target):
    min_coins  = target
    for fives in range(1+target//5):
        fives_val = 5 * fives
        for threes in range(max(1,1+(target-fives_val)//3)):
            threes_val = 3 * threes
            ones = target - fives_val - threes_val
            if(ones >= 0):
                min_coins = min(min_coins, fives+threes+ones)                
    return min_coins

values = list()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    values.append(int(test))
test_cases.close()

#print values
for i in range(len(values)):
    print min_coins_equaling(values[i])


#max_value = max(values)
#hands = list_hands_up_to(max_value)

