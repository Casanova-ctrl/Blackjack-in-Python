from player import Player

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def should_hit(self):
        return self.score < 17

    def show_hand(self, reveal=False):
        print(f"\n{self.name}'s hand:")
        if reveal:
            for card in self.hand:
                print(card)
            print(f"Score: {self.score}")
        else:
            if self.hand:
                print(self.hand[0])
                for _ in self.hand[1:]:
                    print("Hidden Card")
            else:
                print("No cards in hand.")