from itertools import chain
import random

"""
Whot - [20, 20, 20, 20, 20]
Circle - [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14]
Triangle - [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14]
Cross - [1, 2, 3, 5, 7, 10, 11, 13, 14]
Square, [1, 2, 3, 5, 7, 10, 11, 13, 14]
Star, [1, 2, 3, 4, 5, 7, 8]

Power Numbers
20 is a wild card that switches the shape
14 means general market (everyone pick 1 card),
8 means skip the next person,
5 means for the next person to pick up 3 cards (unless you can defend by playing a 5),
2 means the next person picks up 2 cards, and
1 means hold on because I’m going to play whatever card I want to next
"""


def _circle() -> list[str]:
    return [f"Circle {card_num}" for card_num in range(1, 15) if card_num != 6 and card_num != 9]


def _cross() -> list[str]:
    return [f"Cross {card_num}" for card_num in range(1, 15) if card_num != 4
            and card_num != 6 and card_num != 8 and card_num != 9 and card_num != 12]


def _square() -> list[str]:
    return [f"Square {card_num}" for card_num in range(1, 15) if card_num != 4
            and card_num != 6 and card_num != 8 and card_num != 9 and card_num != 12]


def _star() -> list[str]:
    return [f"Star {card_num}" for card_num in range(1, 9) if card_num != 6]


def _triangle() -> list[str]:
    return [f"Triangle {card_num}" for card_num in range(1, 15) if card_num != 6 and card_num != 9]


def _whot() -> list[str]:
    return ["Whot 20" for _ in range(5)]


class Card:
    _cards_list = list(
        chain.from_iterable([_circle(), _cross(), _square(), _star(), _triangle(), _whot()])
    )

    _cards = _cards_list[:]

    @property
    def cards(self) -> list[str]:
        return self._cards

    @cards.setter
    def cards(self, cards) -> None:
        self._cards = cards

    def shuffle_cards(self) -> None:
        random.shuffle(self._cards)

    @staticmethod
    def is_hold_on(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "1"

    @staticmethod
    def is_pick_two(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "2"

    @staticmethod
    def is_pick_three(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "5"

    @staticmethod
    def is_suspension(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "8"

    @staticmethod
    def is_general_market(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "14"

    @staticmethod
    def is_wild_card(card) -> bool:
        return Card.is_valid_card(card) and card.split()[-1] == "20"

    @staticmethod
    def is_power_card(card) -> bool:
        return Card.is_hold_on(card) or Card.is_pick_two(card) or Card.is_pick_three(card) or \
            Card.is_suspension(card) or Card.is_general_market(card) or Card.is_wild_card(card)

    @staticmethod
    def is_valid_card_name(card_name) -> bool:
        return card_name in [_circle.__name__[1:].title(), _cross.__name__[1:].title(),
                             _square.__name__[1:].title(), _star.__name__[1:].title(),
                             _triangle.__name__[1:].title(), _whot.__name__[1:].title()]

    @staticmethod
    def is_valid_card(card) -> bool:
        return card in Card._cards_list
