import random


class Card:
    card_types = []
    possible_colors = ['gold, red, blak, white, blue, green']

    def __init__(self) -> None:
        self.values = {}
        type_and_value = random.choice(list(self.card_types))
        self.points = type_and_value[1]
        self.color = random.choice(self.possible_colors)
        self.append_multiple_colors(type_and_value[0])

    def append_multiple_colors(self, type: list):
        for how_many in type:
            color = random.choice(self.possible_colors)
            self.values[color] = how_many
            self.possible_colors.remove(color)

    def show_card(self):
        return f'color: {self.color}, \n {self.values}'


class CardTierOne(Card):
    card_types = [
        [[2, 1, 1, 1], 0],
        [[1, 1, 1, 1], 0],
        [[4], 1],
        [[2, 1], 0],
        [[1, 2, 2], 0],
        [[1, 3, 1], 0],
        [[3], 0],
        [[2, 2], 0]
    ]


class CardTierTwo(Card):
    card_types = [
        [[3, 2, 3], 1],
        [[1, 4, 2], 2],
        [[6], 3],
        [[3, 5], 2],
        [[5], 2]
    ]


class CardTierThree(Card):
    card_types = [
        [[3, 3, 5, 3], 3],
        [[7], 4],
        [[3, 7], 5],
        [[3, 6, 3], 4]
    ]


class CardCombo:
    possible_cards_combos = [[4, 4], [3, 3, 3]]
    possible_colors = ['gold, red, blak, white, blue, green']
    card_values = {}
    points = 3

    def __init__(self) -> None:
        type = random.choice(self.possible_cards_combos)
        self.append_multiple_colors(type)

    def append_multiple_colors(self, type: list):
        for value in type:
            color = random.choice(self.possible_colors)
            self.card_values[color] = value
            self.possible_colors.remove(color)

    def show_card(self):
        return f'type: {self.type} \n {self.colors}'
