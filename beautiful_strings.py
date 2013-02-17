#!/usr/bin/python
import sys

def max_beauty(line):
    line = line.lower()
    # print line
    contained_letters = set()
    for i in range(len(line)):
        if(line[i].isalpha()):
            # print line[i]
            contained_letters.add(line[i])
    contained_letters_list = sorted(list(contained_letters))
    frequency_list = list()
    for i in range(len(contained_letters_list)):
        letter = contained_letters_list[i]
        occurrences = line.count(letter)
        # print `occurrences` + " copies of " + letter
        frequency_list.append(occurrences)

    frequency_list.sort()
    frequency_list.reverse()
    # print frequency_list

    beautifulness = 0
    letter_val = 26
    for i in range(len(frequency_list)):
        beautifulness += (26-i) * frequency_list[i]
        letter_val -= 1

    return beautifulness

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print max_beauty(test)

test_cases.close()
