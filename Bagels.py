import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"""Bagels: A deductive logic game.
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess it. Clues:
  Pico   - One digit is correct but in the wrong position.
  Fermi  - One digit is correct and in the correct position.
  Bagels - No digit is correct.
""")

    while True:
        secret_num = get_secret_num()
        print(f"I have thought up a number. You have {MAX_GUESSES} guesses.")

        for guess_num in range(1, MAX_GUESSES + 1):
            guess = input(f"Guess #{guess_num}: ")
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Enter a valid {NUM_DIGITS}-digit number.")
                guess = input(f"Guess #{guess_num}: ")

            if guess == secret_num:
                print("You got it!")
                break

            clues = get_clues(guess, secret_num)
            print(clues)
        else:
            print(f"You ran out of guesses. The answer was {secret_num}.")

        if input("Play again? (yes or no): ").lower().startswith('n'):
            break

    print("Thanks for playing!")

def get_secret_num():
    """Generate a random secret number with unique digits."""
    digits = random.sample('0123456789', NUM_DIGITS)
    return ''.join(digits)

def get_clues(guess, secret_num):
    """Generate clues based on the guess and secret number."""
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append(f"Fermi (Position {i + 1})")
        elif guess[i] in secret_num:
            clues.append("Pico")

    return ' '.join(clues) if clues else "Bagels"

if __name__ == "__main__":
    main()
