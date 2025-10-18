#modules
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

#logo hangman
print(logo)

#lives variable init with int number 6
lives = 6

#generate a random word
chosen_word = random.choice(word_list)

#list that stores letters
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

    #input for the players

    guess = input("Guess a letter: ").lower()
    

    #condition case guess already in the list
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    
    #display variable store the letters from users unput
    display = ""

    #if guess not in the chosen_word lives variable reiceive -1
    if guess not in chosen_word:
        #variable lives receive -1
        lives -= 1
        print(F"You guessed {guess}, that's not in the word. You lose a life.")

        #have they run out of lives.
        if lives == 0:
            #finish the loop
            game_over = True
            print(f"***********IT WAS {chosen_word}! YOU LOSE***********")

    print(f"**********{lives}/6 LIVES LEFT************")

    #for each item in the list, do:
    for letter in chosen_word:
        #if letter is equal to guess:
        if letter == guess:
            #display variable receive this letter
            display += letter
            #correct_letters list receive this letter too
            correct_letters.append(letter)
        #other wise, this letter all ready exist in my list, so:
        elif letter in correct_letters:
            #display variable receive this new letter
            display += letter
        #blank the others spaces the word
        else:
            display += "_"
    
    #if display is equal to the word, so finish the program
    if display == chosen_word:
        #loop end
        game_over = True
        print("***********YOU WIN***********")

    print(display)

    print(stages[lives])