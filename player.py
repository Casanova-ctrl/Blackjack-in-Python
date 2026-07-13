class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def receive_card(self, card):
        if card:
            self.hand.append(card)
            self.update_score()

    def update_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            score += card.value
            if card.rank == "Ace":
                aces += 1
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        self.score = score
         
    def show_hand(self):
        print(f"\n{self.name}'s hand:")
        for card in self.hand:
            print(card)
        print(f"Score: {self.score}")

    def reset_hand(self):
        self.hand.clear()
        self.score = 0