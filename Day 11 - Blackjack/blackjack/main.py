import random
from replit import clear
from art import logo

def choices():
    """Returns a random card from the deck."""
    #the Jack/Queen/King all count as 10. There are no jokes.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(carts):
    """Take a list of cards and return the score calculated from the cards"""
    #blackjack sum = 21
    if sum(carts) == 21 and len(carts) == 2:
        return 0

    #the ace can count as 11 or 1.
    if 11 in carts and sum(carts) > 21:
        carts.remove(11)
        carts.append(1)

    return sum(carts)

def result(score_user, score_computer):
    """Compare the user and computer scores and return the result"""
    if (score_user > 21) and (score_computer > 21):
        print("No one won or lost! 😤")
    elif score_user == 0:
        print("You won with a Blackjack! 😎")
    elif score_computer == 0:
        print("You lost with a Blackjack! 😱")
    elif (score_user > score_computer and score_user <= 21) or (score_computer > 21):
        print("You won! 😃")
    elif (score_user < score_computer) or (score_user > 21):
        print("You lost! 😭")
    else:
        print("It's a draw! 🙃")

def play_game():

    print(logo)
    start = True
    user_cards = []
    computer_cards = []
    score_user = 0
    score_computer = 0
    
    for _ in range(2):
        user_cards.append(choices())
        computer_cards.append(choices())
     
    while start:
        score_user = score(user_cards)
        score_computer = score(computer_cards)
        print(f"Your cards: {user_cards}, Score = {score_user}")
        print(f"Computers first card: {computer_cards[0]}")

        if score_user == 0 or score_computer == 0 or score_user >= 21:
            start = False
        else:
            another_card = input("--> Do you want another card? Type 'yes' or 'no': ").lower()
            if another_card == "yes":
                user_cards.append(choices())
            else:
                start = False
            print("--------------------------------------------------------------")
    
    while score_computer != 0 and score_computer < 17:
        computer_cards.append(choices())
        score_computer = score(computer_cards)

    print(f"Your final hand is: {user_cards}, Score = {score_user}")
    print(f"Computer's final hand is: {computer_cards}, Score = {score_computer}")
    result(score_user, score_computer)
            
while input("--> Do you want to play Blackjack game? Type 'yes' or 'no': ").lower() == "yes":
    clear()
    play_game()
