import random
import my_module

random_integer = random.randint(1, 10)
random_float = random.random() #between 0 and 1 (not included)
#if we want to expand the range of random floats, we can multiply it by a number
#e.g. random_float * 5 (between 0 and 5 - not included)

print(random_integer)
print(random_float)
print(my_module.pi)
print("\n")

states_of_america = ["Delaware", "Pencilvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])

states_of_america.append("Rubiland") #adds an item to the end of the list
print(states_of_america[-1]) #the last element of the list

states_of_america[1] = "Pennsylvania" #change the value of an element
print(states_of_america[1])
print("\n")

states_of_america.extend(["Rubiland", "Rubilandia"]) #adds a list to the end of the list
print(states_of_america)
print("\n")

num_states = len(states_of_america) #the number of elements in the list
print(states_of_america[num_states - 1]) #-1 because we count from 0
print("\n")
#lists inside lists
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nect", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomato", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nect", "Apples", "Grapes", "Peaches", "Cher", "Pears"]
vegetables = ["Spinach", "Kale", "Tomato", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][1]) #list zero, element 1