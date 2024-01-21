import random

def generate_word():
    words = ["apple", "banana", "cherry", "dog", "elephant", "python", "programming", "guitar", "jazz", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def get_guess():
    while True:
        guess = input("Угадайте букву: ").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("")

def play_hangman():
    secret_word = generate_word()
    guessed_letters = []
    attempts = 6

    print(а'!")

    while attempts > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(f": {current_display}")
        print(f": {attempts}")

        guess = get_guess()

        if guess in guessed_letters:
            print(".")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(".")

        if set(guessed_letters) == set(secret_word):
            print(.")
            break

    if attempts == 0:
        print(f"И {secret_word}")

if __name__ == "__main__":
    play_hangman()
