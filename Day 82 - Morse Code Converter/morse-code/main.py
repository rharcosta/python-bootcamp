from morse import CODE


def convertcode(sentence):
    sentence = sentence.upper()
    encodedsentence = ""
    for character in sentence:
        encodedsentence += CODE[character] + " "
    print(encodedsentence)


text = input("Please, provide the text: ")
convertcode(text)
