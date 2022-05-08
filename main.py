from board import Board
from player import Player
import sys


class Game:
    game_won = False

    def __init__(self, board, players) -> None:
        self.board = board
        self.players = players
        self.start_the_game()

    def start_the_game(self):
        while not self.game_won:
            for player_id, player in enumerate(self.players, start=1):
                print(f'Player {player_id} turn')
                self.board.check_taken_cards()
                player.take_turn(player, self.board)
                self.check_aristocracy(player)

    def check_aristocracy(self, player):
        for aristocrat in self.aristocracy:
            for key, value  in aristocrat.card_values.values():
                if player.cards[key] >= value:
                    player.aristocracy.append(aristocrat)
                    self.board.aristocracy.remove(aristocrat)


if __name__ == "__main__":
    players_count = int(sys.argv[1])
    players = []
    for i in range(players_count):
        players.append(Player)
    board = Board(players)
    Game(board, players)
