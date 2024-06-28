import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in file.iterrows()}
# print(dictionary)

word = input("Enter a word: ").upper()
my_list = [dictionary[letter] for letter in word]
print(my_list)
