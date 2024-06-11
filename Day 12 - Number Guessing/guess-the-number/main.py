import random
from art import logo
from replit import clear

game_over = False
while game_over == False:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1,100)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attends = 10
    else:
        attends = 5

    win = False
    while (attends > 0) and (win == False):
        print("------------------------------------------------------------")
        print(f"Choose a number between 1-100. You have {attends} attempts.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Number too high! Try again.")
            attends -= 1
        elif guess < number:
            print("Number too low! Try again.")
            attends -= 1
        else:
            print(f"Congratulations! You guessed the number {number}!")
            win = True
    
    answer = input("Do you wanna play again? Type 'yes' or 'no': ").lower()
    if answer == "yes":
        clear()
    else:
        game_over = True
    