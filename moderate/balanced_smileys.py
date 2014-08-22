#!/usr/bin/python
import sys

class smiley_string:
    def __init__(self,istring,value):
        self.as_string = None
        self.as_smiley = None
        self.value     = value

        if(0 == len(istring)):
            return

        if("(" == istring[0]):
#            print "+1"
            self.as_string = smiley_string(istring[1:],self.value+1)
        elif(")" == istring[0]):
#            print "-1"
            self.as_string = smiley_string(istring[1:],self.value-1)
        else:
            self.as_string = smiley_string(istring[1:],self.value)

        if(1 < len(istring)):
            if (":(" == istring[0:2]):
#                print "sad, splitting"
                self.as_smiley = smiley_string(istring[2:],self.value)
            if (":)" == istring[0:2]):
#                print "happy, splitting"
                self.as_smiley = smiley_string(istring[2:],self.value)
        return

    def possibly_balanced(self):
        if((None == self.as_smiley) and (None == self.as_string)):
#            print "bottomed out, returning", (0 == self.value)
            return (0 == self.value)
        if(self.value < 0):
            return False
        if(None == self.as_string):
            return self.as_smiley.possibly_balanced()
        if(None == self.as_smiley):
            return self.as_string.possibly_balanced()
        return (self.as_string.possibly_balanced() or self.as_smiley.possibly_balanced())

def is_balanced(istring):
#    alphabet = "abcdefghijklmnopqrstuvwxyz "
#    for i in range(len(alphabet)):
#        istring = istring.translate(None,alphabet[i])
    my_smiley_string = smiley_string(istring,0)
    if(my_smiley_string.possibly_balanced()):
        print "YES"
    else:
        print "NO"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.lower().rstrip()
    is_balanced(test)

test_cases.close()
