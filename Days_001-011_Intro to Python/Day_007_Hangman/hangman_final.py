# Step 5 - FinalVersion Improving User experience

# import random to choose words
# import hangman_art for the life stages and logo art
# import hangman_words for the word list
# import os to clear after each guess
import random
import hangman_art
from hangman_words import word_list
import os

# Initiate the game, set end state to false, set lives to 6
# pick a word and create blank display based on that word

end = False
lives = 6
word = random.choice(word_list)

display = []
for l in range(len(word)):
    display.append("_")

# Print starting logo and beginning blanks
print(hangman_art.logo)
print("Welcome to hangman!")
print(f"Your word is: {' '.join(display)}")

# Testing code - To make sure we know what word is chosen and can pick an appropriate letter
# print(f'Pssst, the solution is {word}.')

# Initiate empty list for previous guesses, not strictly necessary but nice touch
previous_guess = []

while not end:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    # keep track of the letter guesses so we can output them for the user
    # sort them alphabetically
    if guess in previous_guess:
      print(f"You have already guessed letter {guess}. Please try another letter.")
      print(f"So far you have guessed the following letters: {', '.join(previous_guess)}")
    else:
      previous_guess.append(guess)
      previous_guess = sorted(previous_guess)

    # if letter in word, replace the blanks
    for l in range(len(word)):
        #print(f"Current position: {l}\n Current letter: {word[l]}\n Guessed letter: {guess}")
        if word[l] == guess:
            print(f"The letter {guess} is in the word!")
            display[l] = guess
    
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    
    if guess not in word:
        print(f"This letter {guess} is not in the word. You lose a life.")
        print(f"So far you have guessed the following letters: {', '.join(previous_guess)}")
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # End game once lives reaches 0
    if lives == 0:
        end = True
        print("You lose")

    # End game once all blanks are filled
    if '_' not in display:
        end = True
        print("You win!")

    # Print current life stage
    print(hangman_art.stages[lives])