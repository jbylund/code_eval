#!/usr/bin/python
import sys

def reverse_and_add(iterations, inum):
    if(is_palindrome(inum)):
        return [iterations] + [inum]
    else:
        inum += int(str(inum)[::-1])
        return reverse_and_add(iterations + 1, inum)

# return true if palindrome, otherwise false
def is_palindrome(num_to_test):
    stringval = `num_to_test`
    reverse_stringval = stringval[::-1]
    if(stringval == reverse_stringval):
        return True
    return False

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    ans = reverse_and_add(0, int(test))
    print `ans[0]` + " " + `ans[1]`

test_cases.close()
