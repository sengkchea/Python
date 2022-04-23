#BlackJack 
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True

#CLASSES

#Card class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class
class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.deck.append(created_card)
    
    #Might not need, but for debugging purposes to see what's in a deck
    def __str__(self):
        deck_list = ''

        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_list

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Hand class
class Hand:
    def __init__(self):
        self.cards = [] #start with empty hand
        self.value = 0 #start with value of 0
        self.aces = 0 #keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#Chips class
class Chips:
    def __init__(self):
        self.total = 100 #give player 100 to start
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#FUNCTIONS

#take in player's bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet! '))
        except ValueError: 
            print('Your bet must be an integar.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, your bet cannot exceed your total: {chips.total}')
            else:
                break

#deal card and adjust for aces if necessary
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#ask player to hit or stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("\nWould you like to hit or stand? Press 'h' or 's' ")

        if x.lower() == 'h':
            hit(deck,hand)
        elif x.lower() == 's':
            print('Player stands. Dealer is playing.')
            playing = False
        else:
            print('Sorry, please try again')
            continue
        break

#Functions to display cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("\nDealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("\nPlayer's Hand =",player.value)

#Functions to handle end of game scenarios
def player_busts(chips):
    print('\nPlayer busts!\n')
    chips.lose_bet()

def player_wins(chips):
    print('\nPlayer wins!\n')
    chips.win_bet()

def dealer_busts(chips):
    print('\nDealer busts!\n')
    chips.win_bet()
    
def dealer_wins(chips):
    print('\nDealer wins!\n')
    chips.lose_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie! It's a push.\n")

#Game logic
while True:
    print("Let's play some BlackJack!")
    
    #Create and shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())

    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
        
    #Set up the Player's chips
    player_chips = Chips()
    
    #Prompt the Player for their bet
    take_bet(player_chips)
    
    #Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing: 
        #Prompt for Player to Hit or Stand
        hit_or_stand(new_deck,player_hand)
        
        #Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        #If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    #If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(new_deck,dealer_hand)
            
        #Show all cards
        show_all(player_hand,dealer_hand)
        
        #Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push(player_hand,dealer_hand)
        
    #Inform Player of their chips total 
    print(f"Here is your total: {player_chips.total} \n")

    #Ask to play again
    play_again = input("Would you like to play again? Please enter either 'y' or 'n': ")

    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break
