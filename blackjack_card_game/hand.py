class Hand:
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.value >= 10:
                value += 10
            elif 1 < card.value < 10:
                value += card.value
            elif card.value == 1:
                aces += 1

        if aces > 0:
            for aces in range(aces):
                if value + 11 < 21:
                    value += 11
                else:
                    value += 1

        return value
        
    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

