import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards = [Card(value, suit) for value in Card.VALUE_NAMES.keys() for suit in Card.SUIT_SYMBOLS.keys()]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        cards = [self.cards.pop(0) for card in range(num_cards)]
        
        return cards
        
