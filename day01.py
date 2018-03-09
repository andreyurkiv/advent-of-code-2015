

def get_floor(filename):
    counter = 0
    with open(filename) as file:
        for symbol in file.read():
            if symbol == '(':
                counter += 1
            else:
                counter -= 1
    return counter

def get_basement_index(filename):
    counter = 0
    with open(filename) as file:
        for index, symbol in enumerate(file.read()):
            if symbol == '(':
                counter += 1
            else:
                counter -= 1
            if counter == -1:
                return index + 1

filename = 'puzzle_inputs/day01.txt'

# Get the floor number
print(get_floor(filename))

# Gen an index of the basement pointer
print(get_basement_index(filename))



