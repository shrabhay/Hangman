"""
This program emulates the classic Hangman Word Game.
"""

import random
from hangman_words import word_list
from hangman_art import stages, logo
import os
os.system('clear')

word_to_guess = random.choice(word_list)
user_guesses = []
word_to_guess_list = []
for letter in word_to_guess:
    word_to_guess_list.append(letter)

for letter in word_to_guess:
    user_guesses.append('_')

user_lives = 6
game_on = True
print(logo)

while game_on:
    print(" ".join(user_guesses))
    print("\n")
    user_guess = input("Guess a letter: ").lower()

    os.system('clear')

    if user_guess in user_guesses:
        print(f"You have already guessed {user_guess}. Try a different letter.")
    
    for index, value in enumerate(word_to_guess_list):
        if user_guess == value:
            user_guesses[index] = user_guess
    
    if user_guess not in word_to_guess_list:
        print(f"{user_guess} is not present in the word. You lose a life.")

        user_lives -= 1
        if user_lives == 0:
            game_on = False
            print(stages[user_lives])
            print(f"You lose! The correct word was {word_to_guess}.")

    if '_' not in user_guesses:
        game_on = False
        print(f"You guessed it. The correct word was {word_to_guess}.")

    print(stages[user_lives])
