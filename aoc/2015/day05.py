# Day five

import re

def count_nice(filename):

    nice = 0

    with open(filename) as file:
        for line in file:
            vowels = 0
            doubled = False
            no_syllable = True
            for s in line:
                if s in 'aeiou':
                    vowels += 1
            for i in range(len(line)-1):
                if line[i] == line[i+1]:
                    doubled = True
            for s in ['ab','cd','pq','xy']:
                if s in line:
                    no_syllable = False
            if vowels > 2 and doubled and no_syllable:
                nice += 1
    return nice


def count_nicer(filename):

    nicer = 0

    with open(filename) as file:
        for line in file:

            inbetween = False
            pair = False

            for i in range(len(line)-2):
                if line[i] == line[i+2]:
                    inbetween = True
                if bool(re.match(r".*([a-z]{2}).*\1", line)):
                    pair = True
            if inbetween and pair:

                nicer += 1

    return nicer

filename = 'puzzle_inputs/day05.txt'

print(count_nice(filename))

print(count_nicer(filename))


