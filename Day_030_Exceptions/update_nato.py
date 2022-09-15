import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row['letter']: row['code'] for (index, row) in nato.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("What is your word?:").upper()

nato_word = [nato_dict[letter] for letter in list(word)]
print(nato_word)
