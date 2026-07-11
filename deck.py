import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = [
            "Ace", "2", "3", "4", "5", "6",
            "7", "8", "9", "10",
            "Jack", "Queen", "King"
        ]
        self.values = {
            "Ace": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10
        }       
        self.build_deck()

    def build_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                value = self.values[rank]
                self.cards.append(Card(suit, rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None