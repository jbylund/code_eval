#!/usr/bin/python
import sys

class jline:
    def __init__(self,linecontents):
        self.linelength = len(linecontents)
        self.linecontents = linecontents

test_cases = open(sys.argv[1], 'r')
lineslist = list()
n = 0
for test in test_cases:
    if(0 == n):
        n = int(test)
    else:
        lineslist.append(jline(test.rstrip()))

lineslist = sorted(lineslist, key=lambda jline: -jline.linelength)

for i in range(n):
    print lineslist[i].linecontents

test_cases.close()
