#class import

import random

# Greeting to the user

print("Welcome to Hangman Game!")

# Sample word list
word_list = ["Challenge","bee","baboon","camel","race"]

selected_word = random.choice(word_list)
word_lenght = len(selected_word)

print(f"{selected_word}")

# create a empty list

display_word = []

for _ in range(word_lenght):
    display_word += "_"

# ask user for input

user_input = input("Enter a letter:\n").lower()


#
for position in range(word_lenght):
    letter = selected_word[position]
    if letter == user_input:
        display_word [position] = letter

print(display_word)