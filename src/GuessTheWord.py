import os

# Player 1 inputs the secret word
secret_word = input("Player 1, enter the secret word: ")
secret_word = secret_word.lower()

# Clears the input from player 1
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

    # Player 2 guesses a letter
    guess = input("Player 2, guess a letter: ").lower()

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        print("Correct guess!")
        print("")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        print("")
        max_guesses -= 1

    # Check if the word has been fully guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! Player 2 wins!")
        break

# If the player runs out of guesses
if max_guesses == 0:
    print("Player 2 loses! The secret word was:", secret_word)
