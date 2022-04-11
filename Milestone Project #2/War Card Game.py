import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#dictionary of values used to compare two cards to each other
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
             'Queen':12, 'King':13, 'Ace':14}

#Card class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class
class Deck:
    def __init__(self):
        self.all_cards = [] 

        for suit in suits:
            for rank in ranks:
                #create the Card Object
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    #shuffle newly created deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    #deal one card
    def deal_one(self):
        return self.all_cards.pop()

two_hearts = Card("Hearts","Two")
print(two_hearts)
print(two_hearts.suit)
print(two_hearts.rank)
print(values[two_hearts.rank])
new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card.suit)
new_deck.shuffle()
for card_object in new_deck.all_cards:
    print(card_object)
new_card = new_deck.deal_one()
print(new_card)
print(len(new_deck.all_cards)) 