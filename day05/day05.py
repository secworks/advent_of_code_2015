#!/usr/bin/env python3
#=======================================================================
#
# day05.py
# --------
# Solutions to Advent of Code 2015, day 05.
#
#=======================================================================

import re


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def nice_or_naughty_problem1(s):
#    print("Checkning string", s)
    nice = True

    # Rule 1: At least three vowels:
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for c in s:
        if c in vowels:
            vowels[c] += 1

    if sum(vowels.values()) < 3:
#        print(s, "does not have enough vowels.")
        nice = False

    # Rule 2: At least one letter twice in a row:
    double = False
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]):
            double = True
    if not double:
#        print(s, "does not have at least one letter twice in a row.")
        nice = False


    # Rule 3: ab, cd, pq, or xy not in the string.
    if ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s):
#        print(s, "countains one of the illegal strings.")
        nice = False

    if nice:
        return 'nice'
    else:
        return 'naughty'



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    my_input = get_input("day05_input.txt")
#    my_input = get_input("day05_examples.txt")

    num_nice = 0
    for s in my_input:
        nice_naughty = nice_or_naughty_problem1(s)
        print(s, "is", nice_naughty)
        if nice_naughty == 'nice':
            num_nice += 1

    print("Number of nice strings:", num_nice)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_input = get_input("day05_input.txt")
    my_input = get_input("day05_examples.txt")

    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2015, day 05")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
