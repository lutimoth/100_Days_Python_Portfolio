import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row['letter']: row['code'] for (index, row) in nato.iterrows()}
print(nato_dict)

def generate_nato():
    word = input("What is your word?:").upper()

    try:    
        nato_word = [nato_dict[letter] for letter in list(word)]
    except KeyError:
        print("Only letters please")
        generate_nato()
    else:
        print(nato_word)

generate_nato()
