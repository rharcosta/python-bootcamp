# Data Types
num_lenght = len(input("What is your name? "))
print(type(num_lenght))

# Casting or Conversion

# To String = str()
# To Integer = int()
# To Float = float()
# To Boolean = bool()

# new_num_lenght = str(num_lenght)

print("Your name has " + str(num_lenght) + " characters")

print(2 ** 3) # 2^3
print(round(2.66666, 2)) # round to 2 decimals
print(8 / 3) # float division
print(8 // 3) # integer division

score = 20
score /= 2 # score divided per 2
print(f"Your score is: {score}")