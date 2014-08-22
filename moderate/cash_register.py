#!/usr/bin/python
import sys

class denomination:
    def __init__(self,name,value):
        self.name  = name
        self.value = value

    def __repr__(self):
        return self.name + " " + `self.value`

def make_change(denominations,charge,cash):
    change = cash - charge
    if(0 > change):
        print "ERROR"
        return
    if(0 == change):
        print "ZERO"
        return
    current_denom = 0
    ans = list()
    while(change > 10**-4): # apparently python does not like converting to floats/small numeric values
        while((current_denom + 1 < len(denominations)) and 
              (denominations[current_denom].value > change + 10**-4)):
            current_denom += 1
        change -= denominations[current_denom].value
        ans.append(denominations[current_denom].name)
    ans.sort()
    print ",".join(ans)

denominations = list()
denominations.append(denomination("ONE HUNDRED",100.00))
denominations.append(denomination("FIFTY",50.00))
denominations.append(denomination("TWENTY",20.00))
denominations.append(denomination("TEN",10.00))
denominations.append(denomination("FIVE",5.00))
denominations.append(denomination("TWO",2.00))
denominations.append(denomination("ONE",1.00))
denominations.append(denomination("HALF DOLLAR",0.50))
denominations.append(denomination("QUARTER",0.25))
denominations.append(denomination("DIME",0.10))
denominations.append(denomination("NICKEL",0.05))
denominations.append(denomination("PENNY",0.01))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    charge = float(test.split(";")[0])
    cash = float(test.split(";")[1])
    make_change(denominations,charge,cash)

test_cases.close()
