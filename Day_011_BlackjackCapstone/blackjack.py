############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Imports #####################

from art import logo
import random
player_score = 0
computer_score = 0

start = input('Do you want to play a game of blackjack? y/n ')

if start == 'y':
    game = True
    player_hand = []
    computer_hand = []
    
    #Deal starting hand
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_score = sum(player_hand)
    #Print starting hand and score
    print(f"Your cards: {player_hand}, current score: {player_score}")
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    computer_score = sum(computer_hand)
    #Print onyl computer first card
    print(f"Computer's first card: {computer_hand[0]}")

dealing = True
while game:
    while dealing:
        deal = input("Type 'y' to get another card, type 'n' to pass:")
        
        if deal == 'y':
            player_hand.append(random.choice(cards))
            player_score = sum(player_hand)
            print(f"Your cards: {player_hand}, current score: {player_score}")
            if player_score > 21:
                print(f"Bust, game over, your final score was {player_score}")
                dealing = False
                game = False
                computer = False
        if deal == 'n':
            dealing = False
            game = False
            computer = True
   
    while computer:
        while sum(computer_hand) < 17:
            computer_hand.append(random.choice(cards))
            computer_score = sum(computer_hand)
            print(f"Computer cards: {computer_hand}, computer score: {computer_score}")
        if computer_score == player_score:
            print(f"Push! Nobody wins.")
            computer = False
            game = False
        elif computer_score > player_score:
            print(f"Computer wins! The score was {player_score}-{computer_score}")
            computer = False
            game = False
        else:
            print(f"Player wins! The score was {player_score}-{computer_score}")
            computer = False
            game = False




#Logic for dealing phase
    



