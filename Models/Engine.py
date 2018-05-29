from Models.Board import Board
from Models.Hero import Hero
from Models.Player import Player
import json


class Engine:

    def __init__(self, state, game_over, board_instance=None):
        self.state = state
        self.game_over = game_over
        self.board_instance = board_instance

    def _init_game(self):
        self.init_board()
        self.init_hero()
        self.board_instance.print_board()

    def init_board(self):
        columns = input("nb columns : ")
        rows = input("nb rows : ")

        self.init_hero()

        self.board_instance = Board(columns, rows)

        self.board_instance.add_building()

    def init_player(self):
        playerName = input("Quel est le pseudo du joueur 1: ")
        self.init_hero()
        player1 = Player(playerName)

        playerName = input("Quel est le pseudo du joueur 2: ")
        player2 = Player(playerName)

    def init_hero(self):
        with open("conf/heroes.json") as f:
            data = json.load(f)

        keys = list()

        for key in data:
            keys.append(key)

        print(keys)
