# FileNotFoundError: file doesn't exist
# with open("file.txt") as file:
#     file.read()

# KeyError: the key doesn't exist
# dictionary = {"key": "value"}
# value = dictionary["non_existent_key"]

# IndexError: the index doesn't exist
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError: can't concatenate different types
# text = "abc"
# print(text + 5)

# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there was not an exception
# finally: do this no matter what happens
# raise: creating and showing an error

try:
    file = open("file.txt")
    dictionary = {"key": "value"}
    print(dictionary["non_existent_key"])

except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")
# except IndexError: ...
# except TypeError: ...

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("This is an error that I made up")
