# Step 5 - FinalVersion Improving User experience

# import random to choose words
# import hangman_art for the life stages and logo art
# import hangman_words for the word list
import random
import hangman_art
from hangman_words import word_list

# Initiate the game, set end state to false, set lives to 6
# pick a word and create blank display based on that word
end = False
lives = 6
word = random.choice(word_list)

display = []
for l in range(len(word)):
    display.append("_")

# Print starting logo
print(hangman_art.logo)
print("Welcome to hangman!")
print(display)
# Testing code - To make sure we know what word is chosen and can pick an appropriate letter
print(f'Pssst, the solution is {word}.')

previous_guess = []

while not end:
    guess = input("Guess a letter: ").lower()
    
    if guess in previous_guess:
      print(f"You have already guessed letter {guess}. Please try another letter.")
      print(f"So far you have guessed the following letters: {', '.join(previous_guess)}")
      continue
    else:
      previous_guess.append(guess)
      previous_guess = sorted(previous_guess)

    # Check Guessed letter
    for l in range(len(word)):
        #print(f"Current position: {l}\n Current letter: {word[l]}\n Guessed letter: {guess}")
        if word[l] == guess:
            display[l] = guess
    
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    
    if guess not in word:
        print("This letter is not in the word. Try another.")
        lives -= 1

    #Join all the elements in the list and turn it into a String.
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