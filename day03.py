# Day three

def number_of_houses_visited(filename):

    houses = {}
    x = y = 0

    with open(filename) as file:
        for s in file.read():
            if s == '^':
                y += 1
            elif s == '>':
                x += 1
            elif s == '<':
                x -= 1
            else:
                y -= 1

            if (x,y) not in houses:
                houses[(x,y)] = 1
            else:
                houses[(x,y)] += 1

    return len(houses)

def number_of_houses_visited_by_two(filename):
    houses = {}
    x = [0,0]
    y = [0,0]
    with open(filename) as file:
        for i, s in enumerate(file.read()):
            role =  i % 2
            if s == '^':
                y[role] += 1
            elif s == '>':
                x[role] += 1
            elif s == '<':
                x[role] -= 1
            else:
                y[role] -= 1

            if (x[role],y[role]) not in houses:
                houses[(x[role],y[role])] = 1
            else:
                houses[(x[role],y[role])] += 1


    return len(houses)


filename = 'puzzle_inputs/day03.txt'


print(number_of_houses_visited(filename))

print(number_of_houses_visited_by_two(filename))