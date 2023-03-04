from src.modules.card import Card


class Player:
    """
    pick_card(self, cards, num_of_card) specifies number of cards to be picked up by a player
    place_card(self, card) defines a player playing a card from their stack,
                            returns the card played popped from their stack
    """
    def __init__(self, player_name) -> None:
        self.name = player_name
        self.card_stack: list[Card] = []
        self.win = False
        self.bet_amount = 0

    def pick_card(self, cards, num_of_card) -> None:
        for i in range(num_of_card):
            self.card_stack.append(cards.pop())

    def place_card(self, card) -> Card:
        card_index = self.card_stack.index(card)
        return self.card_stack.pop(card_index)

    @staticmethod
    def has_pick_two(cards) -> bool:
        return any(Card.is_pick_two(card) for card in cards)

    @staticmethod
    def has_pick_three(cards) -> bool:
        return any(Card.is_pick_three(card) for card in cards)
