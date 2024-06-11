import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '$', '%', '&', '(', ')', '*', '+', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

start_program = True
while start_program:
    direction = ""
    while direction != "encode" and direction != "decode":
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))
    shift = shift % 46 #shift greater than number of letters in the alphabet
    
    def caeser(text, shift, direction):
        cipher_text = ""
        for i in text:
            #position of the letter + shift = new letter
            if direction == "encode":
                cipher_index = alphabet.index(i) + shift
            else:
                cipher_index = alphabet.index(i) - shift
            cipher_letter = alphabet[cipher_index]
            cipher_text += cipher_letter
        print(f"\nThe {direction}d text is {cipher_text}.")
    
    caeser(text, shift, direction)
    response = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if response == "no":
        start_program = False
        print("\nGood bye.")