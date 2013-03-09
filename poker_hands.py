#!/usr/bin/python
import sys

class card:
    def __init__(self,istring):
        self.suit = istring[1]
        if(istring[0].isdigit()):
            self.value = int(istring[0])
        elif("T" == istring[0]):
            self.value = 10
        elif("J" == istring[0]):
            self.value = 11
        elif("Q" == istring[0]):
            self.value = 12
        elif("K" == istring[0]):
            self.value = 13
        elif("A" == istring[0]):
            self.value = 14
        else:
            print "Bad input"
        return

    def __repr__(self):
        return str(self.value) + self.suit

    def __gt__(self,othercard):
        return (self.value > othercard.value)

    def __eq__(self,othercard):
        return not((self > othercard) or (othercard > self))

    def __lt__(self,othercard):
        return (othercard > self)

    def __ge__(self,othercard):
        return ((self > othercard) or (self == othercard))

    def __le__(self,othercard):
        return ((self < othercard) or (self == othercard))

class poker_hand:
    def __init__(self,iarray):
        if(5 != len(iarray)):
            return
        self.hand = map(card, iarray)
        self.value_array = list()
        self.value()

    def __gt__(self,otherhand):
        otherhand.value()
        for i in range(min(len(self.value()),len(otherhand.value()))):
            if(self.value_array[i] > otherhand.value_array[i]):
                return True
            if(self.value_array[i] < otherhand.value_array[i]):
                return False
        return False # this is essentially equality

    def __eq__(self,otherhand):
        return not((self > otherhand) or (otherhand > self))

    def __lt__(self,otherhand):
        return (otherhand > self)

    def __ge__(self,otherhand):
        return ((self > otherhand) or (self == otherhand))

    def __le__(self,otherhand):
        return ((self < otherhand) or (self == otherhand))

    def is_straight(self):
        self.hand.sort()
        for i in range(len(self.hand)-1):
            if(self.hand[i].value + 1 != self.hand[i+1].value ):
                return False
        return True

    def is_flush(self):
        suits = set()
        for i in range(1,len(self.hand)):
            suits.add(self.hand[i].suit)
        return (1 == len(suits))

    def value(self):
        if(len(self.value_array) > 0):
            return self.value_array
        straight = self.is_straight()
        flush    = self.is_straight()

        # straight flush
        if(straight and flush):
            self.value_array.append(9)
            self.value_array.append(self.hand[-1].value)
            return self.value_array

        # prelims
        frequencies = [0 for i in range(0,15)]
        values = list()
        for i in range(len(self.hand)):
            frequencies[self.hand[i].value] += 1
            values.append(self.hand[i].value)

        residue = list()
        looking_for = 4 # start by looking for four of a kind
        cards = 0 # start with no cards
        while(cards < len(self.hand)):
            for i in range(len(frequencies)-1,1,-1):
                if(frequencies[i] == looking_for):
                    residue.append(i)
                    cards += looking_for
                    if(cards + looking_for > 5):
                        break
            looking_for -= 1

        # four of a kind
        if(max(frequencies) == 4):
            self.value_array.append(8) # four of a kind
            self.value_array.extend(residue)
            return self.value_array

        # full house
        if(max(frequencies) == 3):
            if(2 in frequencies):
                self.value_array.append(7) # full house
                self.value_array.extend(residue)
                return self.value_array

        # more prelims
        values.sort()
        values = values[::-1] # reverse the values, largest to smallest

        # pure flush
        if(flush):
            self.value_array.append(6)
            self.value_array.extend(residue)
            return self.value_array

        # pure straight
        if(straight):
            self.value_array.append(5)
            self.append(values[0])
            return self.value_array

        # three of a kind
        if(max(frequencies) == 3):
            self.value_array.append(4)
            self.value_array.extend(residue)
            return self.value_array

        # two pair
        if(frequencies.count(2) == 2):
            self.value_array.append(3)
            self.value_array.extend(residue)
            return self.value_array

        if(frequencies.count(2) == 1):
            self.value_array.append(2)
            self.value_array.extend(residue)
            return self.value_array

        if(max(frequencies) == 1):
            self.value_array.append(1)
            self.value_array.extend(residue)
            return self.value_array

        return None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if(0 == len(test.rstrip())):
        continue
    # print test.rstrip()
    left = poker_hand(test.split()[:5])
    right = poker_hand(test.split()[5:])
    if(left > right):
        print "left"
    elif(right > left):
        print "right"
    else:
        print "none"

test_cases.close()
