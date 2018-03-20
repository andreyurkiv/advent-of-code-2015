# Day 13

from collections import defaultdict

filename_t1 = 'puzzle_inputs/day13.txt'

filename_t2 = 'puzzle_inputs/day13_t2.txt'



def parse(filename):
    interactions = defaultdict(list)
    pairs = {}
    with open(filename) as file:
        for line in file:
            words = line.replace('.', '').strip().split(' ')
            interactions[words[0]].append({'name': words[10],
                                           'units': -int(words[3]) if words[2] == 'lose' else int(words[3])})
            pairs[(words[0], words[10])] = -int(words[3]) if words[2] == 'lose' else int(words[3])
    return interactions, pairs


# Task 1
# interactions, pairs = parse(filename_t1)


# Task 2
interactions, pairs = parse(filename_t2)


def next_best(person, chain):
    chain.append(person)

    if len(chain) == len(interactions): return chain

    units = -float('inf')

    for friend in interactions[person]:
        if friend['name'] not in chain:
            if friend['units'] + pairs[(friend['name'], person)] > units:
                units = friend['units'] + pairs[(friend['name'], person)]
                best = friend['name']

    next_best(best, chain)


def sum_interactions(order):
    res = 0
    for i in range(len(order)):
        res += pairs[(order[i], order[i - 1])]
        res += pairs[(order[i], order[0] if i == len(order) - 1 else order[i + 1])]
    return res


def total():
    max_total_satisfaction = 0
    for first in sorted(interactions.keys()):
        chain = []
        next_best(first, chain)
        temp = sum_interactions(chain)
        if temp > max_total_satisfaction:
            max_total_satisfaction = temp
    return max_total_satisfaction


print('Total change in happiness in optimal seating arrangement: {}'.format(total()))







