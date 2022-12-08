#!/usr/bin/env python3
#=======================================================================
#
# day03.py
# --------
# Solutions to Advent of Code 2015, day 03.
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
def update_houses(houses, address):
    if address in houses:
        houses[address] += 1
    else:
        houses[address] = 1
    return houses


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_address(up, down, left, right):
    return "up_" + str(up) + "_down_" + str(down) +\
        "_left_"  + str(left) + "_right_" + str(right)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def follow_directions(directions):
    visited_houses = {}

    up = 0
    down = 0
    left = 0
    right = 0
    curr_address = get_address(up, down, left, right)
    visited_houses = update_houses(visited_houses, curr_address)

    for move in directions:
        if move == "<":
            if right > 0:
                right -= 1
            else:
                left += 1

        elif move == ">":
            if left > 0:
                left -= 1
            else:
                right += 1

        elif move == "^":
            if down > 0:
                down -= 1
            else:
                up += 1

        elif move == "v":
            if up > 0:
                up -= 1
            else:
                down += 1

        curr_address = get_address(up, down, left, right)
        visited_houses = update_houses(visited_houses, curr_address)
    return visited_houses


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def split_directions(directions):
    one = ""
    two = ""
    for i in range(0, (len(directions) - 1), 2):
        one += directions[i]
        two += directions[i + 1]
    return (one, two)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    print("---------")

    # Get input, extract it from the list.
    my_directions = get_input("day03_input.txt")[0]
    visited_houses = follow_directions(my_directions)

    print("Number of visited houses:", len(visited_houses))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("---------")
    # Get input, extract it from the list.
    my_directions = get_input("day03_input.txt")[0]

    (santa_directions, robo_santa_directions) = split_directions(my_directions)

    robo_santa_visited_houses = follow_directions(robo_santa_directions)
    santa_visited_houses = follow_directions(santa_directions)
    santa_visited_houses.update(robo_santa_visited_houses)

    print("Number of combined visited houses:", len(santa_visited_houses))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("Advent of Code 2015, day 03")
print("===========================")
problem1()
problem2()

#=======================================================================
#=======================================================================
