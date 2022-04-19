from hashlib import new
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

#Player class
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        #check if adding multiple cards or just a single card
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#Game setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

#deal cards for both players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print(f'Player {player_one.name} is out of cards. Player {player_two.name} wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'Player {player_two.name} is out of cards. Player {player_one.name} wins!')
        game_on = False
        break
    
    #Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    #while at_war     
    


# two_hearts = Card("Hearts","Two")
# print(two_hearts)
# print(two_hearts.suit)
# print(two_hearts.rank)
# print(values[two_hearts.rank])
# new_deck = Deck()
# first_card = new_deck.all_cards[0]
# print(first_card.suit)
# new_deck.shuffle()
# for card_object in new_deck.all_cards:
#     print(card_object)
# new_card = new_deck.deal_one()
# print(new_card)
# print(len(new_deck.all_cards)) 
# new_player = Player("Seng")
# print(new_player)
# new_player.add_cards(first_card)
# print(new_player)
# new_player.add_cards([first_card, first_card, first_card])
# print(new_player)
# new_player.remove_one()
# print(new_player)