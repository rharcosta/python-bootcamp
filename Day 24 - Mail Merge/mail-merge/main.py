# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
with open("./Input/Letters/starting_letter.txt") as letter:
    my_letter = letter.read()

    txt = open("./Input/Names/invited_names.txt")
    for name in txt.readlines():
        stripped_name = name.strip()
        new_invite = my_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_letter:
            new_letter.write(new_invite)
    txt.close()
