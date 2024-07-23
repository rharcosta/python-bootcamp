from art import logo
from replit import clear

print(logo)

result = True
disc = {}

while result:
    name = input("What's your name? ").upper()
    bid = int(input("What's your bid? $"))
    disc[name] = bid

    def winner(disc):
        max_value = 0
        person = ""
        for key in disc:
            if disc[key] > max_value:
                max_value = disc[key]
                person = key
        print(f"The winner is {person} with a bid of ${max_value}.")
    
    answer = input("There are other users who want to bid? Type 'yes' or 'no'.\n").lower()
    if answer == "no":
        result = False
        winner(disc)
    else:
        clear()
