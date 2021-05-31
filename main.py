#class import

import random


# Hangman stages
live =6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# Greeting to the user

print("Welcome to Hangman Game!")

print(logo)



# Sample word list
word_list = ["Challenge","bee","baboon","camel","race"]

selected_word = random.choice(word_list)
word_lenght = len(selected_word)



# create a empty list

display_word = []

for _ in range(word_lenght):
    display_word += "_"

# try to loop till the user win or lose
game_end = False

while not game_end:
    # ask user for input
    user_input = input("Enter a letter:\n").lower()
    # replace underscore with the right letter
    for position in range(word_lenght):
        letter = selected_word[position]
        if letter == user_input:
            display_word[position] = letter
    print(display_word)

    if "_" not in display_word:
        game_end = True
        print("You Win!")

        live -=1
        if live == 0:
            game_end = True
            print("You Lose")


