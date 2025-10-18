#modules
import random
from hangman_words import word_list

lives = 6

#generate a random word
chosen_word = random.choice(word_list)

correct_letters = []

#generate as many blanks as letters in word
placeholder = ""

#getting the length of the word
length_of_word = len(chosen_word)

#this loop goes through all the letters of the word and add many blanks possible in the placeholder variable.
for position in range(length_of_word):
    placeholder += "_"

#show the users how letters the word have.
print(f"Word to guess {placeholder}")

#ask the user to guess a letter
game_over = False

#this loop finish when game_over is True
while not game_over:
    guess = input("Guess a letter: ")

    display = ""

    if guess not in chosen_word:
        lives -= 1
        
        if lives == 0:
            game_over = True

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if display == chosen_word:
        game_over = True
    


    print(display)