#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo



EASY_MODE = 10
HARD_MODE = 5

#Check answer
def check_answer(guess, answer, turns):
    if guess < answer:
        print("Too low!")
        return turns-1
    elif guess > answer:
        print("Too high!")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")
        again = input("Would you like to play again?")
        if again == 'y':
            game()
        else:
            return


#Set difficulty
def difficulty():
    level = input("Would you like to play easy mode or hard mode? ").lower()
    if level == 'easy':
        return EASY_MODE
    if level == 'hard':
        return HARD_MODE

def game():
    print(logo)
    print("Welcome to guess a number! I am thinking of a number between 1 to 100.")
    answer = randint(1,100)
    
    turns = difficulty()
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} turns left.")
        guess = int(input("What is your guess? "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses! Try again!")
            again = input("Would you like to play again?")
            if again == 'y':
                game()
            else:
                return
        elif guess != answer:
            print("Guess again!")
            
game()
            
        