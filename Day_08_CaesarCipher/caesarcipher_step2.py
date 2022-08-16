from base64 import encode
from distutils import text_file
from operator import index

while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def encrypt(input_text, input_shift):
        word = ""
        for l in input_text:
            pos = alphabet.index(l)
            new_pos = pos + input_shift
            if new_pos < len(alphabet):
                word += alphabet[new_pos]
            else:
                word += alphabet[new_pos - len(alphabet)]
        
        print(f"The encoded text is {word}")

    #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    def decrypt(input_text, input_shift):
        word = ""
        for l in input_text:
            pos = alphabet.index(l)
            new_pos = pos - input_shift
            word += alphabet[new_pos]
        print(f"The decoded text is {word}")

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"


    #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
    # Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

    
    if direction == 'encode':
        encrypt(input_text = text, input_shift = shift)
    else:
        decrypt(input_text = text, input_shift = shift)

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