from replit import clear
import random
import words
import stages

end_of_game = False
print(stages.logo)

chosen_word = random.choice(words.word_list)
#print(chosen_word)

display = []
letters = []

for letter in chosen_word:
  display.append("_")

life = 6
while end_of_game == False:
    guess = input("\nGuess a letter: ").lower()
    clear()
    if guess in display:
        print(f"\nYou already guessed '{guess}' letter. Try again.")
    
    index = 0
    for letter in chosen_word:
        if guess == letter:
            display[index] =  guess
        index += 1
        #print(life)
    
    print(f"\n{' '.join(display)}")
    
    if guess not in chosen_word:
        if guess not in letters:
            letters.append(guess)
            life -= 1
            print(f"\nYou guessed '{guess}', that's not in the word. You lost a life.")
            print(stages.stages[life])
            if life == 0:
                end_of_game = True
                print("You lost!\n")
        else:
            print(f"\nYou already guessed '{guess}' letter. Try again.")
    if "_" not in display:
        end_of_game = True
        print("You won!\n")
    