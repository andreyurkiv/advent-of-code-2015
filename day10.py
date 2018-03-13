# Day 10


def count_and_say(seq, limit, counter=0):
    if counter == limit:
        return seq
    else:
        say = ''
        n = 1
        for i in range(len(seq)):
            try:
                if seq[i+1] != seq[i]:
                    say += str(n) + seq[i]
                    n = 1
                else:
                    n += 1
            except IndexError:
                say += str(n) + seq[-1]
        counter += 1
        return count_and_say(say, limit, counter=counter)


print(len(count_and_say('1321131112', limit=40)))
