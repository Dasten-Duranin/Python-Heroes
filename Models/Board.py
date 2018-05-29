from random import randint
from Models.Building import Building
from Models.Player import Player
from Models.Hero import Hero
import json


class Board:

    def __init__(self, column=10, row=10):
        self.columns = int(column)
        self.rows = int(row)
        self.cells = {}
        self.create_grid()

    def create_grid(self):
        for i in range(self.columns):
            for j in range(self.rows):
                self.cells[(i, j)] = None

    def add_building(self):
        builds = int(self.count_builds_needed())

        while builds != 0:
            rand_column = randint(0, self.columns - 1)
            rand_row = randint(0, self.rows - 1)

            if self.cells[(int(rand_column), rand_row)] is None:
                building = Building((rand_column, rand_row))
                self.cells[(int(rand_column), rand_row)] = building
                builds = builds - 1

    def print_board(self):

        for i in range(0, int(self.rows)):
            r = "|"
            for j in range(0, int(self.columns)):
                if self.cells[(i, j)] is None:
                    r += "    |"
                elif type(self.cells[(i, j)]) is Building:
                    r += " [] |"
                elif type(self.cells[(i, j)]) is Hero:
                    r += " Player |"
            print(r)

    def count_builds_needed(self):
        nb_cases = self.count_cells()
        return nb_cases * 10 / 100

    def count_cells(self):
        return int(self.columns) * int(self.rows)

    def create_new_player(self, name):
        return Player(name)

    def set_player(self, player, hero):
        while True:
            rand_column = randint(0, self.columns - 1)
            rand_row = randint(0, self.rows - 1)

            if self.cells[(rand_column, rand_row)] is None:
                self.cells[(rand_column, rand_row)] = hero
                return True


