# Day six


def the_lights_go_out(filename):

    matrix = [[False for i in range(1000)] for j in range(1000)]

    with open(filename) as file:
        for line in file:

            words = line.split(' ')
            i = 0 if words[0] == 'toggle' else 1
            operation = words[i]
            topx, topy = [int(n) for n in words[i+1].split(',')]
            botx, boty = [int(n) for n in words[i+3].split(',')]

            for i in range(topy, boty+1):
                for j in range(topx, botx+1):
                    if operation == 'toggle':
                        matrix[i][j] = not matrix[i][j]
                    elif operation == 'on':
                        matrix[i][j] = True
                    elif operation == 'off':
                        matrix[i][j] = False
    counter = 0

    for i in range(1000):
        for j in range(1000):
            if matrix[i][j]:
                counter += 1
    return counter


def the_lights_go_brighter(filename):

    matrix = [[0 for i in range(1000)] for j in range(1000)]

    with open(filename) as file:
        for line in file:

            words = line.split(' ')
            i = 0 if words[0] == 'toggle' else 1
            operation = words[i]
            topx, topy = [int(n) for n in words[i+1].split(',')]
            botx, boty = [int(n) for n in words[i+3].split(',')]

            for i in range(topy, boty+1):
                for j in range(topx, botx+1):
                    if operation == 'toggle':
                        matrix[i][j] += 2
                    elif operation == 'on':
                        matrix[i][j] += 1
                    elif operation == 'off':
                        if matrix[i][j] > 0:
                            matrix[i][j] -= 1
    counter = 0

    for i in range(1000):
        for j in range(1000):
            counter += matrix[i][j]
    return counter


filename = 'puzzle_inputs/day06.txt'

print(the_lights_go_out(filename))

print(the_lights_go_brighter(filename))

