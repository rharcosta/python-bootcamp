#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password = []
for letter in range(0, nr_letters): #number of letters the user chose
  password += random.choice(letters) #generating random number and adding to the password
  
for symbol in range(0, nr_symbols):
  password += random.choice(symbols)
  
for number in range(0, nr_numbers):
  password += random.choice(numbers)

#Easy Password
pass_easy = ""
for i in password:
  pass_easy += i
print(f"\nEasy level (order not randomised): {pass_easy}")

#Hard Password
random.shuffle(password)
pass_hard = ""
for i in password:
  pass_hard += i
print(f"\nHard level (order randomised): {pass_hard}")
