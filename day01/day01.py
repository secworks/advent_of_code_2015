#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2015, day 1.
#=======================================================================

DEBUG = True

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    with open(filename,'r') as f:
        for line in f:
            l = line.strip()
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def solutions():
    floor = 0
    pos = 1
    seen = False
    my_input = get_input("day1_input.txt")

    for c in my_input:
        if c == "(":
            floor += 1
        if c == ")":
            floor -= 1
        if floor == -1 and not seen:
            i = pos
            seen = True
        pos += 1

    print("Problem1:")
    print("Final floor: %d" % floor)
    print("")

    print("Problem2:")
    print("First time in basement: %d" % i)
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
solutions()

#=======================================================================
