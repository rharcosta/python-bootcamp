rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import sys

#user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print("\nYou chose Rock.\n")
    print(rock)
elif user_choice == 1:
    print("\nYou chose Paper.\n")
    print(paper)
elif user_choice == 2:
    print("\nYou chose Scissors.\n")
    print(scissors)
else:
    print("Please type 0, 1 or 2 only.")
    sys.exit()

#computer choice
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("\nComputer chose Rock.\n")
    print(rock)
elif computer_choice == 1:
    print("\nComputer chose Paper.\n")
    print(paper)
else:
    print("\nComputer chose Scissors.\n")
    print(scissors)

#tests
# 0 = rock; 1 = paper; 2 = scissors
if user_choice == 0 and computer_choice == 1:
    print("You lose. Paper wins against rock.")
elif user_choice == 0 and computer_choice == 2:
    print("You won. Rock wins against scissors.")
elif user_choice == 1 and computer_choice == 0:
    print("You won. Paper wins against rock.")
elif user_choice == 1 and computer_choice == 2:
    print("You lose. Scissors wins against paper.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose. Rock wins against scissors.")
elif user_choice == 2 and computer_choice == 1:
    print("You won. Scissors wins against paper.")
else:
    print("It's a draw!")
