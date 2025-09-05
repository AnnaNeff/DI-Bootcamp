# Daily challenge: OOP Quizz
# Last Updated: May 5th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP Concepts
# OOP Implementation (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation


# Key Python Topics:

# OOP (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation (random.shuffle())
# Instructions:



# Exercise 1: Quizz
# Answer the following questions:

# What is a class?
# A blueprint for creating objects that defines attributes and methods.

# What is an instance?
# A concrete object created from a class.

# What is encapsulation?
# The bundling of data and methods, restricting direct access to some parts of an object.

# What is abstraction?
# Hiding implementation details and showing only essential features.

# What is inheritance?
# A mechanism where a class can derive attributes and methods from another class.

# What is multiple inheritance?
# When a class inherits from more than one parent class.

# What is polymorphism?
# The ability of different classes to provide different implementations of the same method.

# What is method resolution order (MRO)?
# The order in which Python looks up methods in a hierarchy of classes.

# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
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
