import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in file.iterrows()}
# print(dictionary)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        my_list = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(my_list)


generate_phonetic()
