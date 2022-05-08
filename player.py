from board import Board
class Player:
    aristocracy = []
    tokens = {
        'green': 0,
        'black': 0,
        'red': 0,
        'white': 0,
        'blue': 0,
        'gold': 0
    }
    cards = {
        'green': 0,
        'black': 0,
        'red': 0,
        'white': 0,
        'blue': 0
    }
    your_turn = False
    points = 0
    possible_colors = ('red, blak, white, blue, green')


    def check_hand(self):
        info = f'You have: \n {self.blue_token} blue tokens \n ' \
            f'{self.green_token} green tokens \n {self.red_token} red tokens'

    def take_turn(self, board: Board):
        """One of the main function of the game"""
        self.your_turn = True
        while self.your_turn:
            print('Possible choices: \n 1.Take 3 tokens of diffrent color. \n 2.Take 2 of the same color \n 3.Take card from board')
            turn = input()
            try: 
                if int(turn) > 3 or int(turn) < 1:
                    print('You can only choose a numbet betweeen 1 or 3')
            except Exception:
                print('Input must be a number')
            if turn == '1':
                print(f'What colors? Possible choices: {self.possible_colors}. Write 3 colors separating them with coma')
                colors = input().split(',')
                try: 
                    if int(turn) > 3 or int(turn) < 1:
                        print('You can only choose a numbet betweeen 1 or 3')
                except Exception:
                    print('Input must be a number')    

            if turn == '2':
                print(f'What color? Possible choices: {self.possible_colors}')
                color = input()
            if turn == '3':
                print(f'What card? Possible choices: {board.shown_cards}')
                color = input()
