from card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []
        self.score: int = 0

    def receive_card(self, card: Card | None) -> None:
        if card:
            self.hand.append(card)
            self.update_score()

    def update_score(self) -> None:
        score = sum(card.value for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == "Ace")

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        self.score = score
         
    def show_hand(self) -> None:
        print(f"\n{self.name}'s hand:")
        for card in self.hand:
            print(card)

        print(f"Score: {self.score}")

    def reset_hand(self) -> None:
        self.hand.clear()
        self.score = 0