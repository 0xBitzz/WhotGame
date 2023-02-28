from itertools import chain
import random
"""
'Whot' - [20, 20, 20, 20, 20]
'Circle' - [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14]
'Triangle' - [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14]
'Cross' - [1, 2, 3, 5, 7, 10, 11, 13, 14]
'Square', [1, 2, 3, 5, 7, 10, 11, 13, 14]
'Star', [1, 2, 3, 4, 5, 7, 8]
"""
"""
Power Numbers
20 is a wild card that switches the shape, 14 means general market (everyone pick 1 card),
8 means skip the next person,
5 means for the next person to pick up 3 cards (unless you can defend by playing a 5),
2 means the next person picks up 2 cards, and
1 means hold on because I’m going to play whatever card I want to next
"""


class Circle:
    def __init__(self):
        self.cards = self.__setup_circles()

    @staticmethod
    def __setup_circles():
        return [f"Circle {card_num}" for card_num in range(1, 15) if card_num != 6 and card_num != 9]


class Cross:
    def __init__(self):
        self.cards = self.__setup_cross()

    @staticmethod
    def __setup_cross():
        return [f"Cross {card_num}" for card_num in range(1, 15) if card_num != 4 and card_num != 6 and card_num != 8
                and card_num != 9 and card_num != 12]


class Square:
    def __init__(self):
        self.cards = self.__setup_squares()

    @staticmethod
    def __setup_squares():
        return [f"Square {card_num}" for card_num in range(1, 15) if card_num != 4 and card_num != 6 and card_num != 8
                and card_num != 9 and card_num != 12]


class Star:
    def __init__(self):
        self.cards = self.__setup_stars()

    @staticmethod
    def __setup_stars():
        return [f"Star {card_num}" for card_num in range(1, 9) if card_num != 6]


class Triangle:
    def __init__(self):
        self.cards = self.__setup_triangles()

    @staticmethod
    def __setup_triangles():
        return [f"Triangle {card_num}" for card_num in range(1, 15) if card_num != 6 and card_num != 9]


class Whot:
    def __init__(self):
        self.cards = self.__setup_whots()

    @staticmethod
    def __setup_whots():
        return ["Whot 20" for _ in range(5)]


class Card:
    __cards = list(
        chain.from_iterable(
            [
                Circle().cards, Cross().cards, Square().cards,
                Star().cards, Triangle().cards, Whot().cards
            ]
        )
    )

    def cards(self):
        return self.__cards

    def shuffle_card(self):
        return random.shuffle(self.__cards)

    def share_card(self):
        return self.cards().pop()

    @staticmethod
    def is_power_card(card):
        card = card.split()[1]
        if (card == "1") or (card == "4") or (card == "7") or (card == "8") or (card == "20"):
            return True
        return False
