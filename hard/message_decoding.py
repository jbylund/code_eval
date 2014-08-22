#!/usr/bin/python
import sys

def decode(istring):
    i = len(istring) - 1
    zero_and_one = set()
    zero_and_one.update("0")
    zero_and_one.update("1")
    while(istring[i] in zero_and_one):
        i -= 1
    key = istring[:i+1]
    message = istring[i+1:]
    ans = ""
    pos = 0
    key_len = int(message[pos:pos+3],2)
    while(key_len > 0):
        pos += 3
        # loop over elements
        term_string = "1" * key_len
        offset = 2**(key_len) - (key_len + 1)
        while(term_string != message[pos:pos+key_len]):
            char_id = offset + int(message[pos:pos+key_len],2)
            ans += key[char_id]
            pos += key_len
        pos += key_len # advance past the termination string
        key_len = int(message[pos:pos+3],2)
    return ans

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    test = test.rstrip()
    if(0 == len(test)):
        continue
    print decode(test)
test_cases.close()
