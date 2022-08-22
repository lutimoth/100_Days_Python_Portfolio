from asyncio.streams import FlowControlMixin
from itertools import count
from unicodedata import name
import art
from game_data import data
import random

def random_item():
    return random.choice(data)

# Find the answer
def answer(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'

# Generate the choices
def generate(A, B, score):
    if A:
        A, B = B, random_item()
        output(A, B, score)
    else:
        A, B = random_item(), random_item()
        output(A,B, score)
        
# Compare player guess to choice
def compare(A, B, guess, correct, score):
    if guess == correct:
        score += 1
        generate(A, B, score)
        return score
    else:
        print(f"Your final score is {score}")

# Show player choices and let them choose
def output(A, B, score):
    print(art.logo)
    print(f"{A['name']} is a {A['description']} and is from {A['country']}")
    print(art.vs)
    print(f"{B['name']} is a {B['description']} and is from {B['country']}")
    choice = input("Which one do you think has more followers?: ").upper()
    correct = answer(A,B)
    compare(A, B, choice, correct, score)


# Initialize our choices and start the game
score = 0
A = ""
B = ""
generate(A, B, score)