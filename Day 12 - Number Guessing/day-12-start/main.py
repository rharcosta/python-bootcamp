################### Scope ####################

# enemies = 0

# def increase_enemies():
#   enemies = 2
#   print(f"Local scope: {enemies}")

# increase_enemies()
# print(f"Global escope: {enemies}")

#Python doesn't have a block scope. It means:
#if we create a variable inside a function, it's only available inside that function. But if we create a variable inside a loop or if statement, it's available outside the scope of that block of code.

# if enemies < 2:
#   new_enemies = enemies + 1
# #print outside the if
# print(f"New enemies = {new_enemies}")

#Modifying a global variable
# enemies = 0
# def increase_enemies():
#   global enemies
#   enemies += 2
#   print(f"\nLocal scope: {enemies}")

#or
enemies = 0
def increase_enemies():
  print(f"\nLocal scope: {enemies}")
  return enemies + 2

enemies = increase_enemies()
print(f"Global escope: {enemies}")