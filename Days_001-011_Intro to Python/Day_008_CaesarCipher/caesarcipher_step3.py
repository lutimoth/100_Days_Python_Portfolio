while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
    def caesar(input_text, input_shift, cipher_direction):
        word = ""
        if cipher_direction == 'decode':
                input_shift *= -1
        for l in input_text:
            pos = alphabet.index(l)
            new_pos = pos + input_shift
            if new_pos < len(alphabet):
                word += alphabet[new_pos]
            else:
                word += alphabet[new_pos - len(alphabet)]
        print(f"Here is the {direction}d result: {word}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(input_text=text, input_shift=shift, cipher_direction=direction)

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