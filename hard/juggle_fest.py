#!/usr/bin/python
# This is an example of the stable marriage problem
import sys,operator

def match(ijuggler,icircuit):
    match = 0
    for i in ijuggler.skills:
        if(i in icircuit.skills):
            match += ijuggler.skills[i]*icircuit.skills[i]
    return match

class juggler:
    def __init__(self,name,skills,preferences):
        self.name = name
        self.skills = dict()
        for i in skills:
            skill = i.split(":")
            self.skills[skill[0]] = int(skill[1])
        self.preferences = preferences.split(",")
        self.preferences.reverse()
        self.assigned_circuit = None
        self.current_score = None

    def __repr__(self):
        return self.name # + str(self.skills) + str(self.preferences)

class circuit:
    def __init__(self,name,skills):
        self.name = name
        self.skills = dict()
        for i in skills:
            skill = i.split(":")
            self.skills[skill[0]] = int(skill[1])
        self.assigned_jugglers = list()

    def __repr__(self):
        return self.name + str(self.skills)

jugglers = list()
circuits = list()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip()
    if(0 == len(test)):
        continue
    line = test.split()
    if("C" == line[0]):
        circuits.append(circuit(line[1],line[2:]))
    elif("J" == line[0]):
        jugglers.append(juggler(line[1],line[2:-1],line[-1]))
test_cases.close()

circuit_name_to_int = dict()
for c in xrange(len(circuits)):
    circuit = circuits[c]
    circuit_name_to_int[circuit.name] = c

jugglers_per_circuit = len(jugglers)/len(circuits)
unpaired_jugglers = list()
for i in jugglers:
    unpaired_jugglers.append(i)

while(len(unpaired_jugglers) > 0):
    # each un-engaged juggler proposes
    while(len(unpaired_jugglers) > 0):
        juggler = unpaired_jugglers.pop()
        if(len(juggler.preferences) > 0):
            favored_circuit_num = circuit_name_to_int[juggler.preferences.pop()]
        else:
            favored_circuit_num = 0
            for i in xrange(1,len(circuits)):
                if(len(circuits[i].assigned_jugglers) < len(circuits[favored_circuit_num].assigned_jugglers)):
                    favored_circuit_num = i
        circuits[favored_circuit_num].assigned_jugglers.append(juggler)
        juggler.current_score = match(juggler,circuits[favored_circuit_num])
    # each circuit rejects its least preferred jugglers until it has the correct number
    for circuit in circuits:
        circuit.assigned_jugglers.sort(key=operator.attrgetter('current_score'),reverse=True)
        while(len(circuit.assigned_jugglers) > jugglers_per_circuit):
            juggler = circuit.assigned_jugglers.pop()
            juggler.assigned_circuit = None
            unpaired_jugglers.append(juggler)

circuit = circuits[circuit_name_to_int["C1970"]]
ans = 0
for i in circuit.assigned_jugglers:
    ans += int(i.name.lstrip("J"))
print ans
