# Day 16

import re
from typing import Dict

LETTER_CONSTANTS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


class Day16:

    @staticmethod
    def parse(file_path: str) -> Dict[Dict]:
        """
        Parses the input file and converts to momories dictionary of type:

        {
            1 : {
                    'children': 3,
                    'cats': 7,
                    'samoyeds': 2,
            },
            ...
        }
        :param file_path: path to input file
        :return: dictionary of memories
        """
        memories = {}
        with open(file_path, 'r') as file:
            for line in file:
                sue_id = re.findall(r'[0-9]+:', line)[0][:-1]
                features = re.findall(r'[a-zA-Z]+:\s[0-9]+', line)
                memories[sue_id] = {}
                for feat in features:
                    name, value = feat.split(': ')
                    memories[sue_id][name] = int(value)
        return memories

    @staticmethod
    def intersection(memory: dict) -> int:
        """
        Finds the length of the intersection of 2 dictionaries (taking values into account)
        :param memory: dictionary of id to Sue features
        :return: intersection score
        """
        score = 0
        for k, v in memory.items():
            if k in LETTER_CONSTANTS and LETTER_CONSTANTS[k] == v:
                score += 1
        return score

    @staticmethod
    def intersection_with_ranges(memory) -> int:

        key_to_op = {
            'children':     '__eq__',
            'cats':         '__gt__',
            'samoyeds':     '__eq__',
            'pomeranians':  '__lt__',
            'akitas':       '__eq__',
            'vizslas':      '__eq__',
            'goldfish':     '__lt__',
            'trees':        '__gt__',
            'cars':         '__eq__',
            'perfumes':     '__eq__'
        }
        score = 0
        for key, value in LETTER_CONSTANTS.items():
            if key in memory and getattr(memory[key], key_to_op[key])(LETTER_CONSTANTS[key]):
                score += 1
        return score

    @staticmethod
    def find_sue(memories: dict, corrected: bool = True) -> None:
        """
        Finds the correct aunt Sue
        :param memories: dictionary of Sue id to her features
        :param corrected: whether to used range correction to the task condition
        :return:
        """
        for k, v in memories.items():
            if corrected:
                if Day16.intersection_with_ranges(v) > 2:
                    print(f'{k}: {v}')
            else:
                if Day16.intersection(v) > 2:
                    print(f'{k}: {v}')


if __name__ == '__main__':

    x = Day16.parse('puzzle_inputs/day16.txt')

    # Task 1
    Day16.find_sue(x, corrected=False)
    # 103: {'cars': 2, 'perfumes': 1, 'goldfish': 5}

    # Task 2
    Day16.find_sue(x, corrected=True)
    # 405: {'trees': 8, 'perfumes': 1, 'cars': 2}
