# Day two

def smallest_margin_dimentions(dims):
    return min(dims[0], dims[1]), min(max(dims[0],dims[1]),dims[2])


def get_wrapping_paper_area(filename):
    area = 0
    with open(filename) as file:
        for line in file:
            dims = [int(d) for d in line.split("x")]
            m = [int(d) for d in smallest_margin_dimentions(dims)]
            area += 2*dims[0]*dims[1] + 2*dims[1]*dims[2] + 2*dims[2]*dims[0] + m[0]*m[1]
    return area

def get_ribbon_length(filename):
    length = 0
    with open(filename) as file:
        for line in file:
            dims = [int(d) for d in line.split("x")]
            m = [int(d) for d in smallest_margin_dimentions(dims)]
            length += 2*(m[0]+m[1]) + dims[0]*dims[1]*dims[2]
    return length


filename = 'puzzle_inputs/day02.txt'

print(get_wrapping_paper_area(filename))


print(get_ribbon_length(filename))