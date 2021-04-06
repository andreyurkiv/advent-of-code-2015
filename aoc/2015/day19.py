# Day 19

import re
import random
from typing import List, Tuple

# Test data

REPLACEMENTS_TEST = [
    ('e', 'H'),
    ('e', 'O'),
    ('H', 'HO'),
    ('H', 'OH'),
    ('O', 'HH'),
]

MOLECULE_TEST = 'HOHOHO'

REPLACEMENTS = []

with open('puzzle_inputs/day19.txt', 'r') as file:
    for line in file:
        if len(line) > 1:
            if '=>' in line:
                first, second = line.strip().split(' => ')
                REPLACEMENTS.append((first, second))
            else:
                MOLECULE = line.strip()


class Day19:

    @staticmethod
    def calibrate_molecule(molecule: str, replacements: List[Tuple]) -> int:
        """
        Get number of distinct molecules that can be obtained after single replacement from the list of possible ones.
        :param molecule:
        :param replacements:
        :return:
        """
        molecules = set()
        for source, target in replacements:
            for match in re.finditer(f'(?={source})', molecule):
                s = match.start()
                molecules.add(
                    molecule[:s] + target + molecule[s+len(source):]
                )
        return len(molecules)

    @staticmethod
    def seach_brute(molecule: str, replacements: List[Tuple], current: str = 'e', counter: int = 0):
        """
        Brute force approach
        :param molecule:
        :param replacements:
        :param current:
        :param counter:
        :return:
        """
        if len(current) >= len(molecule):
            if current == molecule:
                yield counter
        else:
            random.shuffle(replacements)
            for source, target in replacements:
                if source in current:
                    for match in re.finditer(f'(?={source})', current):
                        s = match.start()
                        new_current = current[:s] + target + current[s + len(source):]
                        yield from Day19.seach_brute(molecule, replacements, new_current, counter+1)

    @staticmethod
    def search(molecule: str, replacements: List[Tuple]):
        """
        Randomized approach
        :param molecule:
        :param replacements:
        :return:
        """
        target = molecule
        counter = 0
        while target != 'e':
            tmp = target
            for source, dest in replacements:
                index = target.find(dest)
                if index >= 0:
                    target = target[:index] + source + target[index + len(dest):]
                    counter += 1
            if tmp == target:
                target = molecule
                counter = 0
                random.shuffle(replacements)
        return counter


if __name__ == '__main__':
    # Task 1
    assert Day19.calibrate_molecule(MOLECULE_TEST, REPLACEMENTS_TEST) == 7

    print(Day19.calibrate_molecule(MOLECULE, REPLACEMENTS))

    # Task 2
    assert max([x for x in Day19.seach_brute(MOLECULE_TEST, REPLACEMENTS_TEST)]) == 6
    # brute force
    y = min([x for x in Day19.seach_brute(MOLECULE_TEST, REPLACEMENTS_TEST)])
    # randomization
    print(Day19.search(MOLECULE, REPLACEMENTS))

