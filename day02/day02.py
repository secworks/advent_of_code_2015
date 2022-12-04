#!/usr/bin/env python3
#=======================================================================
#
# day02.py
# --------
# Solutions to Advent of Code 2015, day 02.
#
#=======================================================================


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
def get_package_area(package):
    area = 0

    (ls, ws, hs) = package.split('x')
    l = int(ls)
    w = int(ws)
    h = int(hs)

    area1 = l * w
    area2 = w * h
    area3 = h * l

    area += ((2 * area1) + (2 * area2) + (2 * area3))

    if (area1 <= area2) and (area1 <= area3):
        area += area1
    elif (area2 <= area1) and (area2 <= area3):
        area += area2
    else:
        area += area3

    return area


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_ribbon_length(package):
    length = 0

    (ls, ws, hs) = package.split('x')
    l = int(ls)
    w = int(ws)
    h = int(hs)

    length1 = 2 * w + 2 * l
    length2 = 2 * w + 2 * h
    length3 = 2 * h + 2 * l

    bow = w * h * l

    length += bow

    if (length1 <= length2) and (length1 <= length3):
        length += length1
    elif (length2 <= length1) and (length2 <= length3):
        length += length2
    else:
        length += length3

    return length


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")
    my_packages = get_input("day02_input.txt")
#    my_packages = get_input("day02_example.txt")

    total_area = 0
    for package in my_packages:
        total_area += get_package_area(package)

    print("Area needed:", total_area)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")

    my_packages = get_input("day02_input.txt")
#    my_packages = get_input("day02_example.txt")

    total_length = 0
    for package in my_packages:
        total_length += get_ribbon_length(package)

    print("Length needed:", total_length)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2015, day 02")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
