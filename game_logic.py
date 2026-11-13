import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word,
                       guessed_letters):
    """Display the snowman stage for the current
    numer of mistakes the user made"""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)


def play_game():
    """Run an interactive console round of Snowman Meltdown."""
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    won = False
    while mistakes < 3 and not won:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Only one and only alphabetical letters are allowed")
            continue
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        won = True
        for letter in secret_word:
            if letter not in guessed_letters:
                won = False

    display_game_state(mistakes, secret_word, guessed_letters)
    if won:
        print("Yes!!! - you survived the meltdown")
    else:
        print("Owwww 0.o - your Snowman did not"
              " survive your leaky brain")
