import os
import random

print("Welcome to Guess the Word!")
print("Please select a game mode")

# List of words for the single-player mode
animals = ["horse", "cat", "dog", "elephant", "giraffe", "lion", "tiger", "monkey", "snake", "zebra"]

# Ask the user for the game mode
game_mode = input("Enter '1' for single-player mode or '2' for two-player mode: ")

# Choose the secret word based on the game mode
if game_mode == '1':
    secret_word = random.choice(animals)
else:
    secret_word = input("Player 1, enter the secret word: ")
secret_word = secret_word.lower()

# Clear the screen
os.system('cls')

# Create a list to store the guessed letters
guessed_letters = []

# Set the number of allowed guesses
max_guesses = 6

# Game loop
while max_guesses > 0:
    # Display the current state of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # Player guesses a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        max_guesses -= 1

    # Check if the word has been fully guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You win!")
        break