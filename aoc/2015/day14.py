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

        while time > 0:
            if resting:
                time -= self.rest
                resting = False
            else:
                if time <= self.fly:
                    distance += self.speed * time
                    resting = True
                    time = 0
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


deers = parse(file)


def max_distance(deers, time):

    max_distance = 0

    for deer in deers:
        dist = deer.run(time)
        if dist > max_distance:
            max_distance = dist
    return max_distance

print('Task 1')
print('Distance travelled by the fastest deer: {}'.format(max_distance(deers, 2503)))

# Task 2

def get_leaders(scores):
    leaders = []
    lead_distance = max(scores.values())
    for d in scores.keys():
        if scores[d] == lead_distance:
            leaders.append(d)
    return leaders


def max_points(deers, time):

    points = {}

    for deer in deers:
        points[deer.name] = 0

    for t in range(1, time+1):

        scores = {}
        for deer in deers:
            scores[deer.name] = deer.run(t)
        for leader in get_leaders(scores):
            points[leader] += 1
    return points

print('Task 2')
print(max_points(deers, 2503))