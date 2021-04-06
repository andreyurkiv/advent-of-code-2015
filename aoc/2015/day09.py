# Day 9

import math

file = 'puzzle_inputs/day09.txt'


distances = {}
cities = []


def parse(filename):
    with open(filename) as file:
        for line in file:
            words = line.strip().split(' ')
            distances[(words[0], words[2])] = int(words[4])
            distances[(words[2], words[0])] = int(words[4])
            if words[0] not in cities:
                cities.append(words[0])
            if words[2] not in cities:
                cities.append(words[2])


def shortest_route():

    min_distance = math.inf

    for city in cities:
        distance = min_distance_from_the_city(city, cities.copy())
        if distance < min_distance:
            min_distance = distance
    return min_distance


def min_distance_from_the_city(city, cities):
    res = 0
    dest = ''
    dist = math.inf

    del cities[cities.index(city)]
    if len(cities) == 0:
        return 0
    for c in cities:
        if distances[(city, c)] < dist:
            dist = distances[(city, c)]
            dest = c
    return res + dist + min_distance_from_the_city(dest, cities)


def longest_route():

    max_distance = 0

    for city in cities:
        distance = max_distance_from_the_city(city, cities.copy())
        if distance > max_distance:
            max_distance = distance
    return max_distance


def max_distance_from_the_city(city, cities):
    res = 0
    dest = ''
    dist = 0

    del cities[cities.index(city)]
    if len(cities) == 0:
        return 0
    for c in cities:
        if distances[(city, c)] > dist:
            dist = distances[(city, c)]
            dest = c
    return res + dist + max_distance_from_the_city(dest, cities)


# Parse file with the input
parse(file)

# Task 1
print(shortest_route())

# Task 2
print(longest_route())
