# Day 12

import json

filename = 'puzzle_inputs/day12.json'

accumulator = 0

non_red_acc = 0

def count_numbers(filename):

    with open(filename) as file:
        source = json.loads(file.read())
    accumulate_numbers(source)
    accumulate_numbers_without_red_property(source)


def accumulate_numbers(source):

    global accumulator

    if isinstance(source, dict):
        for k, v in source.items():
            if isinstance(v, int):
                accumulator += v
            else:
                accumulate_numbers(v)
    elif isinstance(source, list):
        for e in source:
            if isinstance(e, int):
                accumulator += e
            else:
                accumulate_numbers(e)


def accumulate_numbers_without_red_property(source):

    global non_red_acc

    if isinstance(source, dict):
        if 'red' not in source.values():
            for k, v in source.items():
                if isinstance(v, int):
                    non_red_acc += v
                else:
                    accumulate_numbers_without_red_property(v)
    elif isinstance(source, list):
        for e in source:
            if isinstance(e, int):
                non_red_acc += e
            else:
                accumulate_numbers_without_red_property(e)


count_numbers(filename)


# Task 1
print(accumulator)


# Task 2
print(non_red_acc)