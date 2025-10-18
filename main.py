#modules
import random
from hangman_words import word_list


#generate a random word
chosen_word = random.choice(word_list)

#generate as many blanks as letters in word
placeholder = ""

#getting the length of the word
length_of_word = len(chosen_word)

#this loop goes through all the letters of the word and add many blanks possible in the placeholder variable.
for position in range(length_of_word):
    placeholder += "_"

#show the users how letters the word have.
print(f"Word to guess {placeholder}")
