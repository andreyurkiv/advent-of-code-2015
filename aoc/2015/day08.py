# Day 8

import re

filename = 'puzzle_inputs/day08.txt'
testname = 'puzzle_inputs/testfile.txt'


def output(s):
    print(str(len(s)) + '     ' + s)


def decode(filename, test=False):

    literal = 0
    memory = 0

    with open(filename) as file:
        for line in file:

            line = line.strip()
            if test: output(line)

            literal += len(line)

            quote_free = line[1:-1]
            if test: output(quote_free)

            slash_free = quote_free.replace(r'\\', '?')
            if test: output(slash_free)

            in_quote_free = slash_free.replace(r'\"', '?')
            if test: output(in_quote_free)

            hex_free = re.sub(r'\\x[0-9a-f]{2}', '?', in_quote_free)
            if test: output(hex_free)

            memory += len(hex_free)
    return literal - memory

def encode(filename, test=False):
    literal = 0
    memory = 0

    with open(filename) as file:
        for line in file:

            line = line.strip()
            if test: output(line)

            literal += len(line)

            slash = line.replace('\\', '\\\\')
            if test: output(slash)

            quote = slash.replace('"','\\"')
            if test: output(quote)

            final = '"' + quote + '"'
            if test: output(final)

            memory += len(final)
    return memory - literal



# Task 1
print(decode(filename))

# Task 2
print(encode(filename))



