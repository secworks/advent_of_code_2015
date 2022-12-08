#!/usr/bin/env python3
#=======================================================================
#
# day04.py
# --------
# Solutions to Advent of Code 2015, day 04.
#
#=======================================================================

import hashlib


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_hashstring(secret, num_zeros):
    ctr = 0
    done = False
    target_prefix = '0' * num_zeros

    while not done:
        teststring = secret + str(ctr)
        result = hashlib.md5(teststring.encode())
        digest = result.hexdigest()
        if digest[0 : num_zeros] == target_prefix:
            done = True
        else:
            ctr += 1

    return (ctr, digest)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    (ctr, digest) = find_hashstring("bgvyzdsv", 5)

    print("ctr", ctr, "generates digest", digest)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    (ctr, digest) = find_hashstring("bgvyzdsv", 6)

    print("ctr", ctr, "generates digest", digest)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2015, day 04")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
