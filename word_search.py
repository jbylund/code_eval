#!/usr/bin/python
import sys

class gridsquare:
    def __init__(self,idata):
        self.data = idata
        self.used = False
        return

    def __repr__(self):
        return self.data

class grid:
    def __init__(self,iarray):
        self.data = list()
        for irow in range(len(iarray)):
            self.data.append(list())
            for icol in range(len(iarray[irow])):
                # print iarray[irow][icol]
                self.data[irow].append(gridsquare(iarray[irow][icol]))
                # print self.data[irow][icol]
        return

    def contains(self, istring):
        for irow in range(len(self.data)):
            for icol in range(len(self.data[irow])):
                if(self.contains_at(istring,irow,icol)):
                    return True
        return False

    def contains_at(self,istring,irow,icol):
        # if we reach the end we found it
        if(0 == len(istring)):
            #print "Found it"
            return True

        # if the first thing is not equal to the data at this pos we didn't
        if(istring[0] != self.data[irow][icol].data):
            return False

        if(self.data[irow][icol].used):
            return False

        # otherwise check if we can find the rest at
        #print "using", irow, icol
        self.data[irow][icol].used = True
        for drow in range(-1,1+1):
            if(irow+drow < 0):
                continue
            if(irow+drow >= len(self.data)):
                continue
            for dcol in range(-1,1+1):
                if(abs(drow)+abs(dcol) != 1):
                    continue
                if(icol+dcol < 0):
                    continue
                if(icol+dcol >= len(self.data[irow+drow])):
                    continue
                # at this point we have an in bounds next point
                # print irow+drow,icol+dcol
                if(self.contains_at(istring[1:],irow+drow,icol+dcol)):
                    self.data[irow][icol].used = False                    
                    return True
        #print "un-using", irow, icol
        self.data[irow][icol].used = False
        return False

mygrid = grid([
['A','B','C','E'],
['S','F','C','S'],
['A','D','E','E']
])
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test.rstrip())):
        continue
    # print "finding ", test.rstrip()
    print mygrid.contains(test.rstrip())

test_cases.close()
