# Day 14

file = 'puzzle_inputs/day14.txt'


# Task 1

class Reindeer:

    def __init__(self, name, speed, fly, rest):
        self.name = name
        self.speed = speed
        self.fly = fly
        self.rest = rest

    def __repr__(self):
        return '{0}: speed -> {1}, fly -> {2}, rest -> {3}'.format(self.name, self.speed, self.fly, self.rest)

    def run(self, time):

        resting = False
        distance = 0

        while time >= 0:
            if resting:
                time -= self.rest
                resting = False
            else:
                if time <= self.fly:
                    time = 0
                    distance += self.speed * time
                    resting = True
                else:
                    time -= self.fly
                    distance += self.speed * self.fly
                    resting = True
        return distance


def parse(filename):

    deers = []

    with open(filename) as file:
        for line in file:
            words = line.split(' ')
            deers.append(Reindeer(words[0], int(words[3]), int(words[6]), int(words[13])))
    return deers


def max_distance(deers, time):

    max_distance = 0

    for deer in deers:
        dist = deer.run(time)
        if dist > max_distance:
            max_distance = dist
    return max_distance

print(max_distance(parse(file), 2503))

# Task 2 



