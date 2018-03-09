# Day four

import hashlib

def mine(s):
    counter = 0
    while(True):
        temp = s + str(counter)
        m = hashlib.md5(temp.encode('utf-8'))
        if m.hexdigest().startswith("000000"):
            return counter
        counter += 1


string = 'iwrupvqb'


print(mine(string))