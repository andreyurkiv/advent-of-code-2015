# Day 17

import re
import itertools
from collections import Counter
from typing import List


class Day17:

    @staticmethod
    def parse(file_name: str) -> List[int]:
        """
        Parse input file
        :param file_name: path to file
        :return:
        """
        with open(file_name, 'r') as file:
            return [int(x) for x in re.findall('[0-9]+', file.read())]

    @staticmethod
    def find_all(bench: list, total: int) -> (int, int, int):
        """
        Find all combinations to fill `total` liters using containers available on bench
        :param bench: list of containers
        :param total: amount of liquid to fill
        :return:
        """
        counter = 0
        lengths = []
        for i in range(1, len(bench) + 1):
            for x in itertools.combinations(bench, i):
                if sum(x) == total:
                    counter += 1
                    lengths.append(len(x))
        min_length = min(lengths)
        return counter, min_length, Counter(lengths)[min_length]


if __name__ == '__main__':

    amounts = Day17.parse('puzzle_inputs/day17.txt')

    combinations, length, occurrence = Day17.find_all(amounts, total=150)
    print(f'Ways to fill {150} litres:        {combinations}')
    print(f'Minimum # of containers:        {length}')
    print(f'# of ways ot use {length} containers:  {occurrence}')
