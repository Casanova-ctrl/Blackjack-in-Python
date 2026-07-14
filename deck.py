import random
from card import Card

class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    VALUES = {
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

    def __init__(self) -> None:
        self.cards: list[Card] = []      
        self.build_deck()

    def build_deck(self) -> None:
        for suit in self.SUITS:
            for rank in self.RANKS:               
                self.cards.append(Card(suit, rank, self.VALUES[rank]))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_card(self) -> Card | None:
        return self.cards.pop() if self.cards else None
    
    def __len__(self) -> int:
        return len(self.cards)