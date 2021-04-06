# Day 20

from functools import reduce
from typing import Callable


def factors(n: int) -> set:
    """
    Factors of given number
    :param n:
    :return:
    """
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def house_to_presents_infinite(house_number: int) -> int:
    """
    Sum of factors of `house_number`, multiplied by 10
    :param house_number:
    :return:
    """
    return sum([x for x in factors(house_number)]) * 10


def house_to_presents_limited_to_50(house_number: int) -> int:
    """
    Sum of factors of `house_number`, for which `house_number / factor <= 50, multiplied by 11`
    :param house_number:
    :return:
    """
    return sum([x for x in factors(house_number) if house_number / x <= 50]) * 11


def lowest_house_number(threshold: int, house_to_present_function: Callable) -> int:
    """
    Find lowest house number that contains at least as many presents as threshold
    :param threshold:
    :param house_to_present_function:
    :return:
    """
    position = 1
    while True:
        if house_to_present_function(position) >= threshold:
            return position
        position += 1


if __name__ == '__main__':

    # assert house_to_presents(1) == 10
    # assert house_to_presents(2) == 30
    # assert house_to_presents(3) == 40
    # assert house_to_presents(4) == 70
    # assert house_to_presents(5) == 60
    # assert house_to_presents(7) == 80
    # assert house_to_presents(8) == 150
    # assert house_to_presents(9) == 130

    print(type(lowest_house_number))

    # Task 1
    print(lowest_house_number(33100000, house_to_presents_infinite))
    # 776160

    # Task 2
    print(lowest_house_number(33100000, house_to_presents_limited_to_50))
    # 786240
