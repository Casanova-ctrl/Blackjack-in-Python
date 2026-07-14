from player import Player

class Dealer(Player):
    def __init__(self) -> None:
        super().__init__("Dealer")

    def should_hit(self) -> bool:
        return self.score < 17

    def show_hand(self, reveal: bool = False) -> None:
        if reveal:
            super().show_hand()
        else:
            print(f"\n{self.name}'s hand:")

            if self.hand:
                print(self.hand[0])
                for _ in range(len(self.hand) - 1):
                    print("Hidden Card")
            else:
                print("No cards in hand.")