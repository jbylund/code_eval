#!/usr/bin/python
import sys

def in_dollars(ivalue):
    if(0 == ivalue):
        return "ZeroDollars"
    prefixes = list()
    prefixes.append("")
    prefixes.append("Thousand")
    prefixes.append("Million")
    prefixes.append("Billion")
    prefixes.append("Trillion")
    ans = "Dollars"
    loopnum = 0
    while(ivalue > 0):
        if(ivalue % 1000 != 0):
            ans = hundreds_tens_ones(ivalue % 1000) + prefixes[loopnum] + ans
        ivalue //= 1000
        loopnum += 1
    return ans

# deals with numbers 1-999
def hundreds_tens_ones(ivalue):
    if(0 == ivalue):
        return ""
    if(ivalue < 100):
        return tens_ones(ivalue)
    hundreds = (ivalue % 1000) // 100
    return word_digit(hundreds) + "Hundred" + tens_ones(ivalue % 100)

# given a value between 1-99 this will convert to text
def tens_ones(ivalue):
    if(10 > ivalue):
        return word_digit(ivalue)
    if(10 < ivalue and ivalue < 20):
        return special_word(ivalue%100)
    tens     = (ivalue % 100) // 10
    ones     = (ivalue % 10) // 1
    if(100 > ivalue):
        return word_tens(tens) + word_digit(ones)

# this covers 11-19, as this doesn't quite follow the rule
def special_word(ivalue):
    second_digit = word_digit(ivalue % 10)
    if(15 == ivalue):
        return "Fifteen"
    if(13 == ivalue):
        return "Thirteen"
    if(12 == ivalue):
        return "Twelve"
    if(11 == ivalue):
        return "Eleven"
    if(18 == ivalue):
        return "Eighteen"
    return second_digit + "teen"

# converts a single digit to a word
def word_digit(inum):
    if(0 == inum):
        return ""
    words = ["Zero"]
    words.append("One")
    words.append("Two")
    words.append("Three")
    words.append("Four")
    words.append("Five")
    words.append("Six")
    words.append("Seven")
    words.append("Eight")
    words.append("Nine")
    return words[inum]

# converts a single digit to a word, for tens
def word_tens(inum):
    if(0 == inum):
        return ""
    words = ["Zero"]
    words.append("Ten")
    words.append("Twenty")
    words.append("Thirty")
    words.append("Forty")
    words.append("Fifty")
    words.append("Sixty")
    words.append("Seventy")
    words.append("Eighty")
    words.append("Ninety")
    return words[inum]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    if(0 == len(test)):
        continue
    ivalue = int(test.rstrip())
    print in_dollars(ivalue)

test_cases.close()

