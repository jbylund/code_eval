program:=$(shell ls -t *.cpp|head -n 1)
program:=$(shell basename $(program) .cpp)

$(program) : $(program).cpp
	g++ -Wall -O2 -g -o $(program) $(program).cpp
