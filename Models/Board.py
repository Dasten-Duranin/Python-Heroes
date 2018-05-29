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
        self.players = {}

        self.create_grid()

    def create_grid(self):
        for i in range(self.columns):
            for j in range(self.rows):
                self.cells[(i, j)] = None

    def add_building(self):
        builds = int(self.count_builds_needed())

        while builds != 0:
            randColumn = randint(0, self.columns - 1)
            randRow = randint(0, self.rows - 1)

            if self.cells[(int(randColumn), randRow)] is None:
                building = Building((randColumn, randRow))
                self.cells[(int(randColumn), randRow)] = building
                builds = builds - 1

    def print_board(self):
        for i in range(0, int(self.rows)):
            r = "|"
            for j in range(0, int(self.columns)):
                print('cell')
                print(self.cells[(i, j)])
                if self.cells[(i, j)] is None:
                    r += "    |"
                elif type(self.cells[(i, j)]) is Building:
                    r += " [] |"
                elif type(self.cells[(i, j)]) is Hero:
                    r += " P1 |"
            print(r)

    def count_builds_needed(self):
        nbCases = self.count_cells()
        return nbCases * 10 / 100

    def count_cells(self):
        return int(self.columns) * int(self.rows)

    def create_new_player(self, name):
        player = Player(name)
        return player

    def set_player(self, player_name, heroData):
        print(hero)
        while True:
            randColumn = randint(0, self.columns - 1)
            randRow = randint(0, self.rows - 1)

            if self.cells[(int(randColumn), randRow)] is None:
                #heroModel = Hero('name', hero.life, hero.strength, hero.speed, hero.canFly, self.cells[(int(randColumn), randRow)])
                self.cells[(int(randColumn), randRow)] = heroModel
                self.players[player_name] = hero
                return True


