programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#printing the value of a key
#print(programming_dictionary["Function"])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#create an empty dictionary
empty_dictionary = {}

#editing a value of a key in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

for key in programming_dictionary:
    print(key) #only the key
    print(programming_dictionary[key]) #the value of the key

# nesting = {key1: list[],
#            key2: dict{},
#           }
#it's not possible for a key receive many values, only in a list or a dictionary
travel_log = {"France": ["Paris", "Lyon", "Marseille"],
              "Germany": ["Berlin", "Hamburg", "Stuttgart"]
             }
#cities visited with the number of times they were visited (dictionary)
travel_log = {"France": {"Paris": 4, "Lyon": 2, "Marseille": 2},
              "Germany": {"Berlin": 5, "Hamburg": 3, "Stuttgart": 1}
             }

travel_log = {"France": {"cities_visited":["Paris", "Lyon", "Marseille"], "total_of_visits": 8},
              "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_of_visits": 9}
             }

travel_log = [
    {
        "country":"France", 
        "cities_visited":["Paris", "Lyon", "Marseille"], 
        "total_of_visits": 8
    },
    
    {
        "country":"Germany", 
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_of_visits": 9
    }
]