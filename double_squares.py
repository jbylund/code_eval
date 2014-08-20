#!/usr/bin/python
import sys

def num_of_ways_to_express_as_sum_of_squares(thenum):
  exprs = 0
  for i in squares:
    if i*2 > thenum:
      continue
    if (thenum - i) in squares:
      exprs += 1
  return exprs

i = 0
squares = set()
while i*i <= 2147483647:
  squares.add(i*i)
  i += 1

with open(sys.argv[1],'r') as infile:
  infile.readline()
  for line in infile:
    thenum = int(line.strip())
    print num_of_ways_to_express_as_sum_of_squares(thenum)

