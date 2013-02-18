#!/usr/bin/python
import sys

## return true if the string is well-formed, which is not defined
## in the problem definition
#def valid_parens(ilist):
##    print ilist
#    if(0 == len(ilist)):
#        return True
#    if(0 != (len(ilist) % 2)):
#        return False
#    first_char = ilist.pop(0)
#    last_char = mirror(ilist.pop())
##    print "first char = ", first_char
##    print "last char = ", last_char
##    print ilist
#    return ((first_char == last_char) and (valid_parens(ilist)))

def mirror(ichar):
    if(ichar == "("):
        return ")"
    if(ichar == "["):
        return "]"
    if(ichar == "{"):
        return "}"
    if(ichar == ")"):
        return "("
    if(ichar == "]"):
        return "["
    if(ichar == "}"):
        return "{"

def valid_parens(ilist):
    matched = True
    if(0 != (len(ilist) % 2)):
        return False
    while(matched and (0 != len(ilist))):
        matched = False
        i = 0
        while((not matched) and (i < (len(ilist) - 1))):
            if(ilist[i] == mirror(ilist[i+1])):
                ilist.pop(i) # remove i
                ilist.pop(i) # remove i+1 (which was downshifted)
                matched = True
            i += 1
    return matched


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
#    # 'test' represents the test case, do something with it
    print valid_parens(list(test))

test_cases.close()
