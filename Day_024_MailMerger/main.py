#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Open the name files
with open('./Input/Names/invited_names.txt') as names:
    name_list = names.readlines()
    # print(name_list)

# Strip the newlines from each name
clean_names = [name.strip() for name in name_list]
# print(clean_names)


#Loop through names in list and create new letters
for name in clean_names:
    with open('./Input/Letters/starting_letter.txt') as letter:
        standard_letter = letter.readlines()
    standard_letter[0] = standard_letter[0].replace("[name]", name)
    print(standard_letter)
    new_letter = ' '.join(standard_letter)
    with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as final_letter:
        final_letter.write(new_letter)
        
