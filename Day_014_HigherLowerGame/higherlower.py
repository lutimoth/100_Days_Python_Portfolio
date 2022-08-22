from asyncio.streams import FlowControlMixin
from itertools import count
from unicodedata import name
import art
from game_data import data
import random

def random_item():
    return random.choice(data)
#   name, follower_count, description, country = choice.values()


# Find the answer
def answer(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'
    
def generate():
    if A:
        A, B = B, random_item()
        output(A,B)
    else:
        A, B = random_item(), random_item()
        return A, B

score = 0

# Compare player guess to choice
def compare(A, B, guess, correct, score):
    if guess == correct:
        score += 1
        A, B = B, random_item()
        output(A,B, score)
        return score
    else:
        print(f"Your final score is {score}")

# Show player choices and let them choose
def output(A,B):
    print(f"{A['name']} is a {A['description']} and is from {A['country']}")
    print(f"{B['name']} is a {B['description']} and is from {B['country']}")
    choice = input("Which one do you think has more followers?: ").upper()
    correct = answer(A,B)
    score = compare(A, B, choice, correct, score)

# def player_choice():
#     choice = input("Which one do you think has more followers?: ").upper()
#     correct = answer(A,B)
#     compare(choice, correct)

# Initialize our choices
A = random_item()
B = random_item()

output(A,B, score)