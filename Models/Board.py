from random import randint
from Models.Building import Building

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
                if self.cells[(i, j)] is None:
                    r += "    |"
                elif type(self.cells[(i, j)]) is Building:
                    r += " [] |"
                # elif type(self.cells[(i, j)]) is player.Player:
                # r += "AAA|"
            print(r)

    def count_builds_needed(self):
        nbCases = self.count_cells()
        return nbCases * 10 / 100

    def count_cells(self):
        return int(self.columns) * int(self.rows)

