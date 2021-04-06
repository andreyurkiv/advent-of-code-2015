# Day 15

from typing import Dict

class Day15:

    def parse(self, filename: str) -> Dict[Dict]:
        """
        Parses the input file and converts to dictionary format:

        {
            "Butterscotch": {
                "capacity": -1,
                "durability": -2,
                "flavor": 6,
                "texture": 3,
                "calories": 8
            },
            ...
        }
        :param filename: path to input file
        :return: ingredients dictionary
        """
        ingredients = {}
        with open(filename, 'r') as file:
            for line in file:
                ingredient, prop_str = line.split(':')
                props = {}
                for prop in prop_str.strip().replace(', ', ',').split(','):
                    name, value = prop.split(' ')
                    props[name] = int(value)
                ingredients[ingredient] = props
        return ingredients

    def additions(self, parts: int, total: int, existing: tuple = ()):
        """
        Generator that outputs all possible combinations of numbers that sum up to `total`
        :param parts: numbers in combination
        :param total: desired sum of numbers
        :param existing: used for sequential addition of numbers to the combination tuple
        :return: generates tuples of number combinations
        """
        if parts == 1:
            yield existing + (total - sum(existing),)
        else:
            for i in range(1, total - sum(existing)):
                yield from self.additions(parts - 1, total, existing + (i,))

    def score(self, ingredients: dict, amounts: tuple) -> (int, int):
        """
        Calculates the cookie score for given amounts of ingredients
        :param ingredients: ingredients dictionary
        :param amounts: a tuple of mass amounts for each ingredient
        :return: cookie score and number of calories
        """
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0

        for amount, properties in zip(amounts, ingredients.values()):
            capacity += amount * properties['capacity']
            durability += amount * properties['durability']
            flavor += amount * properties['flavor']
            texture += amount * properties['texture']
            calories += amount * properties['calories']

        capacity = 0 if capacity < 0 else capacity
        durability = 0 if durability < 0 else durability
        flavor = 0 if flavor < 0 else flavor
        texture = 0 if texture < 0 else texture

        return capacity * durability * flavor * texture, calories

    def best_recipe(self, filename: str, mass: int = 100) -> int:
        """
        Calculates the maximum cookie score for given cookie mass and ingredients
        :param filename: path to ingredients file
        :param mass: mass of the cookie in grams
        :return: max score
        """
        ingredients = self.parse(filename)
        max_score = 0
        for amounts in self.additions(len(ingredients), mass):
            curr_score, _ = self.score(ingredients, amounts)
            if curr_score > max_score:
                max_score = curr_score
        return max_score

    def best_recipe_with_calories(self, filename: str, mass: int = 100, desired_calories: int = 500) -> int:
        """
        Calculates the maximum cookie score for given cookie mass, ingredients and amount of calories
        :param filename: path to ingredients file
        :param mass: mass of the cookie in grams
        :param desired_calories:
        :return: max score
        """
        ingredients = self.parse(filename)
        max_score = 0
        for amounts in self.additions(len(ingredients), mass):
            curr_score, calories = self.score(ingredients, amounts)
            if curr_score > max_score and calories == desired_calories:
                max_score = curr_score
        return max_score


if __name__ == '__main__':
    solution = Day15()

    print(solution.best_recipe('puzzle_inputs/day15_test.txt'))
    # 62842880

    print(solution.best_recipe('puzzle_inputs/day15.txt'))
    # 13882464

    print(solution.best_recipe_with_calories('puzzle_inputs/day15_test.txt'))
    # 57600000

    print(solution.best_recipe_with_calories('puzzle_inputs/day15.txt'))
    # 11171160
