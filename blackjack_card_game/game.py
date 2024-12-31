from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def place_bet(self):
        while self.bet is None:
            self.bet = int(input("Place your bet: "))

            if self.bet < 1:
                print("The minimum bet is $1.")
                self.bet = None
            elif self.bet > self.player.balance:
                print("You do not have sufficient funds.")
                self.bet = None

    def player_turn(self):
        while True:
            hit = self.hit_stay()
            if not hit:
                break

            new_card = self.deck.deal(1)[0]
            self.player.hit(new_card)
            print("You are dealt:", new_card)
            print("You now have:", self.player.get_str_hand())

            if self.player.hand.get_value() > 21:
                return True
            
            elif self.player.hand.get_value() == 21:
                self.blackjack()
                return False

        return False

    def dealer_turn(self):
        print(f"The dealer has: {self.dealer.get_str_hand()}")

        while self.dealer.hand.get_value() <= 16:
            new_card = self.deck.deal(1)[0]
            self.dealer.hit(new_card)
            print(f"The dealer hits and is dealt: {new_card}")
            print("The dealer has:", self.dealer.get_str_hand())

        if self.dealer.hand.get_value() > 21:
            return True

        return False

    def hit_stay(self):
        while True:
            hit_stay = input("Would you like to hit or stay? ").lower()

            if hit_stay == "hit" or hit_stay == "stay":
                break

            print("That is not a valid option.")

        return hit_stay == "hit"

    def determine_winner(self):
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()

        if player_value == dealer_value:
            print("You tie. Your bet has been returned.")
        elif player_value > dealer_value:
            print(f"You win ${self.bet}!")
            self.player.balance += self.bet
        elif player_value < dealer_value:
            print(f"The dealer wins, you lose ${self.bet} :(")
            self.player.balance -= self.bet

    def blackjack(self):
        if self.dealer.hand.get_value() == 21:
            self.player.balance += self.bet
            print(
                "Both you and the dealer have Blackjack, you tie. Your bet has been returned.")
            return True
        
        if self.player.hand.get_value() != 21:
            return False
        
        self.player.balance += self.bet * 1.5
        print(f"Blackjack! You win ${self.bet * 1.5} :)")
        
        return True

    def start_game(self):
        if self.player.balance < 0:
            print("You've ran out of money. Please restart this program to try again. Goodbye.")
            return
        
        self.place_bet()
        self.deck.create_deck()
        self.deck.shuffle()
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))

        print(f"You are dealt: {self.player.get_str_hand()}")
        print(f"The dealer is dealt: {self.dealer.get_str_hand()[0:2]}, Unknown")
        
        if self.blackjack():
            return

        player_lost = self.player_turn()
        if player_lost:
            self.player.balance -= self.bet
            print(f"Your hand value is over 21 and you lose ${self.bet} :(")
            return

        dealer_lost = self.dealer_turn()
        if dealer_lost:
            self.player.balance += self.bet
            print(f"The dealer busts, you win ${self.bet} :)")
            return

        self.determine_winner()

        

