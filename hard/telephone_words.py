#!/usr/bin/python
import sys

key = list()
key.append(['0'])
key.append(['1'])
key.append(['a','b','c'])
key.append(['d','e','f'])
key.append(['g','h','i'])
key.append(['j','k','l'])
key.append(['m','n','o'])
key.append(['p','q','r','s'])
key.append(['t','u','v'])
key.append(['w','x','y','z'])

class digit:
    def __init__(self,digit):
        self.value = digit
        self.rep   = 0
        return

    def next(self):
        self.rep = (self.rep + 1) % len(key[self.value]) # advance and possibly cycle
        return (0 == self.rep) # return true if you cycled

    def __repr__(self):
        return key[self.value][self.rep]
        
class phone_number:
    def __init__(self,inum):
        idigit_array = map(int,list(str(inum)))
        self.digit_array = list()
        for i in range(len(idigit_array)):
            self.digit_array.append(digit(idigit_array[i]))

    def __repr__(self):
        return "".join(map(str,self.digit_array))

    # advance to the next number, return true
    # if done, false if need to "carry"
    def next(self):
        i = len(self.digit_array)-1
        # while need to "carry"
        while(True == self.digit_array[i].next()):
            i -= 1
            if(i < 0):
                return False
        return True

    def list_possibilities(self):
        possible_words = list()
        possible_words.append(str(self))
        while(self.next()):
            possible_words.append(str(self))
        # because of the keyboard, we happen to know everything is already
        # properly ordered, however we could sort here were that not the case
        print ",".join(possible_words)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    phone_number(int(test)).list_possibilities()

test_cases.close()
