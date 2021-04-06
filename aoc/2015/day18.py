# Day 18

import os
from typing import List

GRID_SIZE = 100
CORNERS_ALWAYS_ON = False


class GameOfLife:
    def __init__(self, input_file: str):
        """
        Initializes the grid using the data from input file
        :param input_file: path to input file
        """
        self.grid = self.empty()
        self.iteration = 0

        with open(input_file, 'r') as file:
            for i, line in enumerate(file):
                self.grid[i + 1] = list('.' + line.strip() + '.')

        if CORNERS_ALWAYS_ON:
            self.grid[1][1] = '#'
            self.grid[1][100] = '#'
            self.grid[100][1] = '#'
            self.grid[100][100] = '#'

    def empty(self) -> List[List]:
        """
        Returns empty grid with padding of 1
        :return:
        """
        return [['.' for _ in range(GRID_SIZE + 2)] for _ in range(GRID_SIZE + 2)]

    def lights_on(self) -> int:
        """
        Checks how many lights on the grid are on
        :return:
        """
        return ''.join([''.join(line) for line in self.grid]).count('#')

    def lights_on_roi(self, i: int, j: int) -> (int, bool):
        """
        Returns # of lights on on the 3x3 grid centered at i,j and the value of i,j cell
        :param i: row
        :param j: column
        :return:
        """

        arr = [
            self.grid[i-1][j-1],
            self.grid[i-1][j],
            self.grid[i-1][j+1],
            self.grid[i][j-1],
            self.grid[i][j+1],
            self.grid[i+1][j-1],
            self.grid[i+1][j],
            self.grid[i+1][j+1]
        ]

        central = self.grid[i][j]
        return arr.count('#'), True if central == '#' else False

    def step(self) -> None:
        """
        Performs single iteration of Conway's Game of Life
        :return: None
        """
        temp = self.empty()
        for i in range(1, GRID_SIZE + 1):
            for j in range(1, GRID_SIZE + 1):
                lights, was_on = self.lights_on_roi(i, j)

                if was_on:
                    if lights in [2, 3]:
                        temp[i][j] = '#'
                    else:
                        temp[i][j] = '.'
                else:
                    if lights == 3:
                        temp[i][j] = '#'

        if CORNERS_ALWAYS_ON:
            temp[1][1] = '#'
            temp[100][100] = '#'
            temp[1][100] = '#'
            temp[100][1] = '#'

        self.grid = temp
        self.iteration += 1

    def __str__(self) -> str:
        """
        Textual representation of the grid with counters
        :return:
        """
        return '\n'.join([''.join(line) for line in self.grid]) + \
               f'\nIteration: {self.iteration}' \
               f'\nLights on: {self.lights_on()}'

    def run(self, iterations: int) -> None:
        """
        Run game for n iterations
        :param iterations:
        :return: None
        """
        for i in range(iterations + 1):
            os.system('clear')
            print(gif)
            gif.step()


if __name__ == '__main__':
    gif = GameOfLife(input_file='puzzle_inputs/day18.txt')
    gif.run(iterations=10000)
