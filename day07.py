# Day 7

def toint(s):
    return int(s) if s.isdigit() else s


def parse(filename):

    with open(filename) as file:

        operation = {}
        for line in file:

            words = line.strip().split(' ')

            if 'NOT' in line:
                operation[words[3]] = {'negative': True,
                                       'operation': None,
                                       'op1': toint(words[1]),
                                       'op2': None}
            elif 'AND' in line:
                operation[words[4]] = {'negative': None,
                                       'operation': words[1],
                                       'op1': toint(words[0]),
                                       'op2': toint(words[2])}
            elif 'OR' in line:
                operation[words[4]] = {'negative': None,
                                       'operation': words[1],
                                       'op1': toint(words[0]),
                                       'op2': toint(words[2])}
            elif 'LSHIFT' in line:
                operation[words[4]] = {'negative': None,
                                       'operation': words[1],
                                       'op1': toint(words[0]),
                                       'op2': toint(words[2])}
            elif 'RSHIFT' in line:
                operation[words[4]] = {'negative': None,
                                       'operation': words[1],
                                       'op1': toint(words[0]),
                                       'op2': toint(words[2])}
            else:
                operation[words[2]] = {'negative': False,
                                       'operation': None,
                                       'op1': toint(words[0]),
                                       'op2': None}
    return operation





filename = 'puzzle_inputs/day07.txt'
# print(parse(filename))


operations = parse(filename)
# operations = parse(testfile)

wirevalues = {}

def calc(wire):

    if wire in wirevalues:
        print("Got {} from the dictionary".format(wire))
        return wirevalues[wire]

    else:
        e = operations[wire]
        if e['operation'] is None:
            if e['negative']:
                if isinstance(e['op1'], int):
                    wirevalues[wire] = ~e['op1'] & 0xFFFF
                    return ~e['op1'] & 0xFFFF
                else:
                    return ~calc(e['op1']) & 0xFFFF
            else:
                if isinstance(e['op1'], int):
                    wirevalues[wire] = e['op1']
                    return e['op1']
                else:
                    return calc(e['op1'])
        else:
            if e['operation'] == 'AND':
                if isinstance(e['op1'], int):
                    if isinstance(e['op2'], int):
                        wirevalues[wire] = e['op1'] & e['op2']
                        return e['op1'] & e['op2']
                    else:
                        return e['op1'] & calc(e['op2'])
                else:
                    if isinstance(e['op2'], int):
                        return calc(e['op1']) & e['op2']
                    else:
                        return calc(e['op1']) & calc(e['op2'])
            if e['operation'] == 'OR':
                if isinstance(e['op1'], int):
                    if isinstance(e['op2'], int):
                        wirevalues[wire] = e['op1'] | e['op2']
                        return e['op1'] | e['op2']
                    else:
                        return e['op1'] | calc(e['op2'])
                else:
                    if isinstance(e['op2'], int):
                        return calc(e['op1']) | e['op2']
                    else:
                        return calc(e['op1']) | calc(e['op2'])
            if e['operation'] == 'RSHIFT':
                if isinstance(e['op1'], int):
                    wirevalues[wire] = e['op1'] >> e['op2']
                    return e['op1'] >> e['op2']
                else:
                    return calc(e['op1']) >> e['op2']
            if e['operation'] == 'LSHIFT':
                if isinstance(e['op1'], int):
                    wirevalues[wire] = e['op1'] << e['op2']
                    return e['op1'] << e['op2']
                else:
                    return calc(e['op1']) << e['op2']

print(calc('a'))
