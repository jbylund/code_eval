#!/usr/bin/python
import sys

class uri:
    def __init__(self,istring):
        self.protocol = istring.split(":")[0].lower()
        self.hostname = istring.split(":")[1].lstrip("/").split("/")[0].split(":")[0].lower()
        self.port = 80
        if(len(istring.split(":")) >= 3):
            port_string = istring.split(":")[2].split("/")[0]
            if(len(port_string) > 0):
                self.port = int(port_string)

        self.location = "/".join(istring.split("/")[3:])
        self.location = dehex(self.location)

    def __repr__(self):
        return self.protocol + "://" + self.hostname + ":" + `self.port` + "/" + self.location

def dehex(istring):
    while(-1 != istring.find("%",0,len(istring)-3)):
        iindex = istring.find("%",0,len(istring)-3)
        weirdchar = istring[iindex+1:iindex+3].lower()
        istring = istring[:iindex] + chr(int(weirdchar,16)) + istring[iindex+3:]
    return istring

def is_equal(suri1, suri2):
    uri1 = uri(suri1)
    uri2 = uri(suri2)
    return(str(uri1) == str(uri2))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test)):
        continue
    test = test.rstrip()
    print is_equal(test.split(";")[0],test.split(";")[1])

test_cases.close()
