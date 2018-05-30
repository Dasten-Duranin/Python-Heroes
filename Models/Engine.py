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
        self.board_instance.print_board()

    def init_board(self):
        columns = input("Nombre de colonnes : ")
        rows = input("Nombre de lignes : ")
        self.board_instance = Board(columns, rows)
        self.board_instance.add_building()
        self.init_player()

    def init_player(self):
        player_name = input("Quel est le pseudo du joueur 1: ")
        player = self.board_instance.create_new_player(player_name)
        self.create_hero_for_user(player)

        player_name = input("Quel est le pseudo du joueur 2: ")
        player = self.board_instance.create_new_player(player_name)
        self.create_hero_for_user(player)

    def create_hero_for_user(self, player):
        with open("conf/heroes.json") as f:
            config = json.load(f)

        heroes = {}
        i = 0

        for hero in config:
            print('[ ' + str(i) + ' ]' + ' ' + hero)
            heroes[i] = hero
            i += 1

        print(heroes)

        while True:
            hero_id = input('Choisissez le personnage ? ')
            hero = Hero.get_by_conf(heroes[int(hero_id)])

            if hero is None:
                print('Invalid Hero')
            else:
                print('LA')
                print(hero)
                self.board_instance.set_player(player.get_name(), hero)
                return True

