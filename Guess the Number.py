import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print("Guess the Number Game!")
print("I'm thinking of a number between 1 and 100. You have 10 tries.")

# Loop for 10 guesses
for attempts in range(10):
    guess = int(input(f"Attempt {attempts + 1}/10: Enter your guess: "))
    if guess == secret_number:
        print("Yay! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Game over! The number was {secret_number}.")
