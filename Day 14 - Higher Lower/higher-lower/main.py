import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0
B = random.choice(data)

def compare(A, B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'

start = True
while start:
    A = B #for the next round, A is the previous B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    print(logo)
    print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"\nAgainst B: {B['name']}, a {B['description']}, from {B['country']}.")
    answer = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    clear()
    print(logo)
    
    if (answer == 'A' and compare(A, B) == 'A') or (answer == 'B' and compare(A, B) == 'B'):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        start = False
