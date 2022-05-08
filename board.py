from cards import CardTierOne, CardCombo, CardTierThree, CardTierTwo
import random
import pprint

class Board:
    """
    Board is dependent on how many players play the game.
    It's a place, where you can see avaible tokens and cards.
    Tokens and cards are generated at start of the game
    """
    possible_colors = ('gold, red, blak, white, blue, green')
    """Rules of the game can be changed here"""
    number_of_tier_one = 40
    number_of_tier_two = 30
    number_of_tier_three = 20
    number_of_aristocracy = 5
    number_of_tokens = 7
    number_of_gold_tokens = 5
    number_of_playing_cards = 4
    tokens_for_two_players = 4
    tokens_for_three_players = 5
    aristocracy_for_two_players = 3
    aristocracy_for_three_players = 4
    """List that will change during the game"""
    cards_tier_one = []
    cards_tier_two = []
    cards_tier_three = []
    shown_tier_one = []
    shown_tier_two = []
    shown_tier_three = []
    shown_cards = [[]]
    aristocracy = []
    players = []
    """Tokens that will be used this game"""
    tokens = {
        'green': 0,
        'black': 0,
        'red': 0,
        'white': 0,
        'blue': 0,
        'gold': 0
    }

    def __init__(self, players: list) -> None:
        """
        I'm not sure what is better in that instance - multiple for i in range
        or one for i in range with multiple ifs.
        """
        self.players = players
        self._validate_players_count(len(players))

        self._generate_cards()
        self._set_token_numbers()
        self._show_cards()

    def show_board(self):
        pprint()

    def check_taken_cards(self):
        if len(self.shown_tier_one) != self.number_of_playing_cards:
            self._append_random_and_delete(self.shown_tier_one, self.cards_tier_one)
        if len(self.shown_tier_two) != self.number_of_playing_cards:
            self._append_random_and_delete(self.shown_tier_one, self.cards_tier_two)
        if len(self.shown_tier_three) != self.number_of_playing_cards:
            self._append_random_and_delete(self.shown_tier_one, self.cards_tier_three)


    def _show_cards(self):
        for i in range(self.number_of_playing_cards):
            self._append_random_and_delete(self.shown_tier_one, self.cards_tier_one)
            self._append_random_and_delete(self.shown_tier_two, self.cards_tier_two)
            self._append_random_and_delete(self.shown_tier_three, self.cards_tier_three)
            # self.shown_tier_one.append(random.choice(self.cards_tier_one))
            # self.shown_tier_two.append(random.choice(self.cards_tier_two))
            # self.shown_tier_three.append(random.choice(self.cards_tier_three))
    
    def _append_random_and_delete(self, appending_list: list, random_list: list):
        random_choice = random.choice(random_list)
        appending_list.append(random_choice)
        random_list.remove(random_choice)

    def _set_token_numbers(self):
        for color in self.possible_colors:
            self.tokens[color] = self.number_of_tokens
        self.tokens['gold'] = self.number_of_gold_tokens

    def _validate_players_count(self, players_count):
        if players_count < 2 or players_count > 4:
            raise Exception(
                "Only number of players between 2 and 4 can play the game.")

        if players_count == 2:
            self.number_of_aristocracy = self.aristocracy_for_two_players
            self.number_of_tokens = self.tokens_for_two_players

        if players_count == 3:
            self.number_of_aristocracy = self.aristocracy_for_three_players
            self.number_of_tokens = self.tokens_for_three_players

    def _generate_cards(self):
        for i in range(self.number_of_tier_one):
            self.cards_tier_one.append(CardTierOne)
            if i < self.number_of_tier_one:
                self.cards_tier_two.append(CardTierTwo)
            if i < self.number_of_tier_two:
                self.cards_tier_two.append(CardTierTwo)
            if i < self.number_of_tier_three:
                self.cards_tier_three.append(CardTierThree)
            if i < self.number_of_aristocracy:
                self.aristocracy.append(CardCombo)
