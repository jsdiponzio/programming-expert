from player import Player
from dealer import Dealer
from game import Game

def main():
    STARTING_BALANCE = 500
    player = Player(STARTING_BALANCE)
    dealer = Dealer()
    new_game = True

    print("Welcome to Blackjack!\n")

    while new_game == True:
        new_hand = input(f"You are starting with ${player.balance}. Would you like to play a hand? ")
        if new_hand.lower() == "yes":
            game = Game(player, dealer)
            game.start_game()
        else:
            new_game == False

if __name__ == '__main__':
    main()