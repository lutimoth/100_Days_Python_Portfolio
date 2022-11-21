from art import logo

# Import and print the logo from art.py when the program starts.
print(logo)

# Start of continuation
while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Take input text, input shift, and direction (encode vs decode)
    def caesar(input_text, input_shift, cipher_direction):
        word = ""
        if cipher_direction == 'decode':  # If decode, take negative shift
                input_shift *= -1
        for char in input_text: 
            if char in alphabet: # If character is in the alphabet, code it, if not just add to string
                pos = alphabet.index(char)
                new_pos = pos + input_shift
                if new_pos < len(alphabet):
                    word += alphabet[new_pos]
                else:
                    word += alphabet[new_pos - len(alphabet)]
            else:   
                word += char
        print(f"Here is the {direction}d result: {word}")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Add modulo to prevent shifts > 26 so we do not run into shifting errors
    caesar(input_text=text, input_shift=shift%26, cipher_direction= direction)

    
    # While loop to assist with restarting the program in case user wishes to run it again. 
    while True:
        repeat = input("Run again? (y/n): ")
        if repeat in ('y','n'):
            break
        print("Invalid input.")
    if repeat == 'y':
        continue
    else:
        print("Goodbye")
        break


    
