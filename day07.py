# Day 7


def toint(s):
    return int(s) if s.isdigit() else s


def parse(filename):
    with open(filename) as file:
        nodes = {}
        for line in file:

            words = line.strip().split(' ')

            if 'NOT' in line:
                nodes[words[3]] = {'negative': True,
                                   'operation': None,
                                   'op1': toint(words[1]),
                                   'op2': None}
            elif 'AND' in line:
                nodes[words[4]] = {'negative': None,
                                   'operation': words[1],
                                   'op1': toint(words[0]),
                                   'op2': toint(words[2])}
            elif 'OR' in line:
                nodes[words[4]] = {'negative': None,
                                   'operation': words[1],
                                   'op1': toint(words[0]),
                                   'op2': toint(words[2])}
            elif 'LSHIFT' in line:
                nodes[words[4]] = {'negative': None,
                                   'operation': words[1],
                                   'op1': toint(words[0]),
                                   'op2': toint(words[2])}
            elif 'RSHIFT' in line:
                nodes[words[4]] = {'negative': None,
                                   'operation': words[1],
                                   'op1': toint(words[0]),
                                   'op2': toint(words[2])}
            else:
                nodes[words[2]] = {'negative': False,
                                   'operation': None,
                                   'op1': toint(words[0]),
                                   'op2': None}
    return nodes


def calc(wire):
    if wire in wirevalues.keys():
        return wirevalues[wire]

    else:
        e = nodes[wire]
        if e['operation'] is None:
            if e['negative']:
                if isinstance(e['op1'], int):
                    res = ~e['op1'] & 0xFFFF
                else:
                    res = ~calc(e['op1']) & 0xFFFF
            else:
                if isinstance(e['op1'], int):
                    res = e['op1']
                else:
                    res = calc(e['op1'])
        else:
            if e['operation'] == 'AND':
                if isinstance(e['op1'], int):
                    if isinstance(e['op2'], int):
                        res = e['op1'] & e['op2']
                    else:
                        res = e['op1'] & calc(e['op2'])
                else:
                    if isinstance(e['op2'], int):
                        res = calc(e['op1']) & e['op2']
                    else:
                        res = calc(e['op1']) & calc(e['op2'])
            if e['operation'] == 'OR':
                if isinstance(e['op1'], int):
                    if isinstance(e['op2'], int):
                        res = e['op1'] | e['op2']
                    else:
                        res = e['op1'] | calc(e['op2'])
                else:
                    if isinstance(e['op2'], int):
                        res = calc(e['op1']) | e['op2']
                    else:
                        res = calc(e['op1']) | calc(e['op2'])
            if e['operation'] == 'RSHIFT':
                if isinstance(e['op1'], int):
                    res = e['op1'] >> e['op2']
                else:
                    res = calc(e['op1']) >> e['op2']
            if e['operation'] == 'LSHIFT':
                if isinstance(e['op1'], int):
                    res = e['op1'] << e['op2']

                else:
                    res = calc(e['op1']) << e['op2']
    wirevalues[wire] = res
    return res


filename = 'puzzle_inputs/day07.txt'

nodes = parse(filename)

# Part one
wirevalues = {}
print(calc('a'))

# Part two
wirevalues = {'b': 16076}
print(calc('a'))




