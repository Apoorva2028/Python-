import random
import time
import playsound

# Function to play the sound corresponding to a letter
def play_sound(letter):
    playsound.playsound(f'c:/Users/APOORVA M/Downloads/sound{letter}.wav')

print("Sound Mimic Game! Memorize the sequence of letters (A, S, D, F).")
input("Press Enter to start...")

pattern = ""
while True:
    # Add a random letter to the pattern
    pattern += random.choice("ASDF")

    # Show the pattern and play sounds
    print("\nPattern: ", " ".join(pattern))
    for letter in pattern:
        play_sound(letter)
        time.sleep(0.5)

    # Get user input
    response = input("Repeat the pattern: ").upper()

    if response != pattern:
        print(f"Incorrect! The correct pattern was: {pattern}")
        print(f"Your score: {len(pattern) - 1}")
        break

    print("Correct! Get ready for the next round.")
    time.sleep(1)
