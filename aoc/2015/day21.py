# Day 21

import random
from math import factorial
from functools import reduce


class Store:

    def __init__(self):
        self.weapons = {
            'Dagger':     {'Cost': 8,  'Damage': 4, 'Armor': 0},
            'Shortsword': {'Cost': 10, 'Damage': 5, 'Armor': 0},
            'Warhammer':  {'Cost': 25, 'Damage': 6, 'Armor': 0},
            'Longsword':  {'Cost': 40, 'Damage': 7, 'Armor': 0},
            'Greataxe':   {'Cost': 74, 'Damage': 8, 'Armor': 0}
        }

        self.armor = {
            'Leather':    {'Cost': 13,  'Damage': 0, 'Armor': 1},
            'Chainmail':  {'Cost': 31,  'Damage': 0, 'Armor': 2},
            'Splintmail': {'Cost': 53,  'Damage': 0, 'Armor': 3},
            'Bandedmail': {'Cost': 75,  'Damage': 0, 'Armor': 4},
            'Platemail':  {'Cost': 102, 'Damage': 0, 'Armor': 5}
        }

        self.rings = {
            'Damage+1':   {'Cost': 25,  'Damage': 1, 'Armor': 0},
            'Damage+2':   {'Cost': 50,  'Damage': 2, 'Armor': 0},
            'Damage+3':   {'Cost': 100, 'Damage': 3, 'Armor': 0},
            'Defence+1':  {'Cost': 20,  'Damage': 0, 'Armor': 1},
            'Defence+2':  {'Cost': 40,  'Damage': 0, 'Armor': 2},
            'Defence+3':  {'Cost': 80,  'Damage': 0, 'Armor': 3}
        }

        for x in ['weapons', 'armor', 'rings']:
            self.__setattr__(f'{x}_count', len(getattr(self, x)))

        self.weapons_range = [1]
        self.armor_range   = [0, 1]
        self.rings_range   = [0, 1, 2]

    @staticmethod
    def comb(r: int, n: int) -> int:
        return int(factorial(n) / (factorial(n - r) * factorial(r)))

    def count_comb(self) -> int:
        return reduce(
            lambda x, y: x * y, [
                sum([
                        Store.comb(r, getattr(self, f'{x}_count')) for r in getattr(self, f'{x}_range')
                    ]) for x in ['weapons', 'armor', 'rings']
            ]
        )

    def random_equipment(self) -> dict:
        equipment = {}
        for eq in ['weapons', 'armor', 'rings']:
            eq_dict = getattr(self, eq)
            rand_amount = random.choice(getattr(self, f'{eq}_range'))
            rand_bundle = random.sample(list(eq_dict.keys()), rand_amount)
            for name in rand_bundle:
                equipment[name] = eq_dict[name]
        return equipment


class Character:

    def __init__(self):
        self.hit_points = 0
        self.damage = 0
        self.armor = 0

    def attack(self, other):
        points = self.damage - other.armor
        points = points if points > 1 else 1
        other.hit_points = other.hit_points - points

    def __str__(self):
        return f'HP: {self.hit_points} >>> {self.damage} ||| {self.armor}'


class Player(Character):
    def __init__(self, equipment: dict):
        super().__init__()
        self.hit_points = 100
        self.cost = 0

        for name, features in equipment.items():
            self.damage += features['Damage']
            self.armor += features['Armor']
            self.cost += features['Cost']

        self.unique = str(sorted(equipment.keys()))


class Boss(Character):
    def __init__(self):
        super().__init__()
        self.hit_points = 104
        self.damage = 8
        self.armor = 1


class Battlefield:

    def __init__(self):
        self.store = Store()
        self.eq_to_cost = {}

    def find(self, function) -> int:
        """
        Find min or max price in eq_to_cost dictionary values
        :param function: `min` or `max`
        :return:
        """
        return function(filter(lambda x: x > 0, self.eq_to_cost.values()))

    def run(self, player: Player, boss: Boss, winning_target: bool):
        while player.hit_points > 0 and boss.hit_points > 0:
            player.attack(boss)
            boss.attack(player)

        if boss.hit_points < 1:
            self.eq_to_cost[player.unique] = player.cost if winning_target else -1
        else:
            self.eq_to_cost[player.unique] = -1 if winning_target else player.cost

    def experiment(self, winning_target):

        combinations = self.store.count_comb()

        while len(self.eq_to_cost) < combinations:
            equipment = self.store.random_equipment()
            eq_id = str(sorted(equipment.keys()))
            if eq_id not in self.eq_to_cost:
                self.run(Player(equipment), Boss(), winning_target)

        if winning_target:
            print(f'Best winning set of equipment costs: {self.find(min)} of gold')
        else:
            print(f'Worst losing set of equipment costs: {self.find(max)} of gold')

        self.eq_to_cost.clear()


if __name__ == '__main__':

    field = Battlefield()
    field.experiment(winning_target=True)        
    field.experiment(winning_target=False)
