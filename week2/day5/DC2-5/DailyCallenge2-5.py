import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]

    def shuffle(self):
        if len(self.cards) != 52:
            print("Warning: Deck is not full before shuffling!")
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
       
        else:
            first_card = self.cards[-1]
            self.cards.remove(first_card) 

        return first_card

deck = Deck()
print("deck has", len(deck.cards))
deck.shuffle()
print("Card: ", deck.deal())
print("Deck contain:", len(deck.cards), "cards")
print("Card: ", deck.deal())
print("Card: ", deck.deal())
print("Deck contain:", len(deck.cards), "cards")
