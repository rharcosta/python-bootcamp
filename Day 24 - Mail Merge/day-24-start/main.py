# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with this method I don't need to close the file
# mode= w(write), a(append), r(read)
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# creating a new file
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

# Absolute Path
# \Users\rubia\python-bootcamp\Day 24 - Mail Merge\my_file.txt
# \Users\rubia\Downloads\my_file.txt
# ../../Downloads/my_file.txt

# Relative Path
# open("my_file.txt") or open("./my_file.txt")
