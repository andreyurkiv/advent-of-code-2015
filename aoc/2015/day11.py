# Day 11


values = {}

for s in 'abcdefghijklmnopqrstuvwxyz':
    values[ord(s)] = s


def is_valid(pw):

    doubles = 0
    alphabet = False
    symbols = False

    for i in range(len(pw)-1):
        if i == 0:
            if pw[i] == pw[i+1]:
                doubles += 1
        else:
            if pw[i] == pw[i + 1]:
                if pw[i:i+2] != pw[i-1:i+1]:
                    doubles += 1

    for i in range(len(pw)-2):
        if ord(pw[i]) == ord(pw[i+1]) - 1 == ord(pw[i+2]) - 2:
            alphabet = True

    for s in 'iol':
        if s in pw:
            symbols = True

    return doubles > 1 and alphabet and not symbols


def next_in_order(pw):
    letters = list(reversed(list(pw)))

    res = letters.copy()
    forward = 0

    for i,l in enumerate(letters):
        if i == 0:
            if l == 'z':
                res[i] = 'a'
                forward = 1
            else:
                res[i] = values[ord(l)+1]
        else:
            if forward:
                if res[i] == 'z':
                    res[i] = 'a'
                    forward = 1
                else:
                    res[i] = values[ord(l)+1]
                    forward = 0

    return ''.join(s for s in list(reversed(res)))


def next_valid_password(password):

    while not is_valid(password):
        password = next_in_order(password)
    return password


# Task 1
print(next_valid_password('cqjxjnds'))

# Task 2
print(next_valid_password(next_in_order('cqjxxyzz')))
