# Greeting to the user
import random

print("Welcome to Hangman Game!")

print("Let me generate a word to guess")


# Sample word list

word_list = ["bee","baboon","camel","race"]

selected_word = random.choice(word_list)

print(selected_word)

# ask user for input

user_input = input("Enter a letter").lower()

for selected_word in selected_word:
    if user_input == selected_word:
        print("Right")
    else:
        print("Wrong")
