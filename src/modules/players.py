from src.modules.card import Card


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.card_stack: list[Card] = []
        self.num_of_wins = 0
        self.bet_amount = 0

    def pick_card(self, cards, num_of_card):
        for i in range(num_of_card):
            self.card_stack.append(cards.pop())

    def place_card(self, card):
        card_index = self.card_stack.index(card)
        return self.card_stack.pop(card_index)
