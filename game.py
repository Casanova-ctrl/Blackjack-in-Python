from deck import Deck
from dealer import Dealer
from player import Player

BLACKJACK = 21


class Game:
    def __init__(self):
        name = input("Enter your name: ")
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck: Deck | None = None

    def play_game(self) -> None:
        while True:
            self.initial_deal()

            if self.check_blackjack():
                if not self.play_again():
                    break
                continue

            if not self.player_turn():
                if self.play_again():
                    continue
                break

            if self.dealer_turn():
                self.determine_winner()

            if not self.play_again():
                break

    def initial_deal(self) -> None:
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck = Deck()
        self.deck.shuffle()
        self.player.receive_card(self.deck.deal_card())
        self.dealer.receive_card(self.deck.deal_card())
        self.player.receive_card(self.deck.deal_card())
        self.dealer.receive_card(self.deck.deal_card())
        
        print("\n==============================")
        print("      NEW ROUND")
        print("==============================")
        
        self.player.show_hand()
        self.dealer.show_hand()

    def player_turn(self) -> bool:
        print("\n==============================")
        print(f"      {self.player.name.upper()}'S TURN")
        print("==============================")
        while True:
            action = input("\nDo you want to hit or stand? (h/s): ").strip().lower()
            if action == "h":
                self.player.receive_card(self.deck.deal_card())
                self.player.show_hand()

                if self.player.score > BLACKJACK:
                    print("\nYou bust! Dealer wins.")
                    return False
                
            elif action == "s":
                return True
            else:
                print("\nInvalid input. Please enter 'h' or 's'.")

    def dealer_turn(self) -> bool:
        print("\n==============================")
        print("      DEALER'S TURN")
        print("==============================")
        while self.dealer.should_hit():
            self.dealer.receive_card(self.deck.deal_card())

        self.dealer.show_hand(reveal=True)

        if self.dealer.score > BLACKJACK:
            print("\nDealer bust! You win.")
            return False
        return True
    
    def determine_winner(self) -> None:
        player_score = self.player.score
        dealer_score = self.dealer.score
        print("\n========== FINAL SCORES ==========")
        print(f"{self.player.name}: {player_score}")
        print(f"Dealer: {dealer_score}")

        if player_score > dealer_score:
            print("\nYou win!")

        elif player_score < dealer_score:
            print("\nDealer wins.")
        else:
            print("\nIt's a tie!")

    def check_blackjack(self) -> bool:
        player_blackjack = self.player.score == BLACKJACK
        dealer_blackjack = self.dealer.score == BLACKJACK

        if player_blackjack and dealer_blackjack:
            self.dealer.show_hand(reveal=True)
            print("\nBoth have Blackjack!")
            print("It is a tie!")
            return True
        
        elif player_blackjack:
            self.dealer.show_hand(reveal=True)
            print("\nBlackjack!")
            print(f"{self.player.name} wins!")
            return True

        elif dealer_blackjack:
            self.dealer.show_hand(reveal=True)
            print("\nDealer has Blackjack!")
            print("Dealer wins!")
            return True
        
        return False

    def play_again(self) -> bool:
        while True:
            answer = input("\nDo you want to play again? (y/n): ").strip().lower()
            if answer == "y":
                return True
            
            elif answer == "n":
                print("\nThanks for playing!")
                return False
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")