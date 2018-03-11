import re

filename = 'puzzle_inputs/day08.txt'
testname = 'puzzle_inputs/test.txt'


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
    return literal, memory

def encode(filename, test=False):
    pass


display, in_memory  = decode(filename)


print(display)
print(in_memory)
print(display - in_memory)



