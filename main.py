from deck import Deck

deck = Deck()

print(len(deck.cards))

deck.shuffle()

for card in deck.cards[:5]:
    print(card)

card = deck.deal_card()

print(card)
print(len(deck.cards))