import random, sys, time

def get_difficulty():
    """Get the difficulty level from the user."""
    while True:
        print('Select difficulty level: Easy, Intermediate, Hard')
        level = input('> ').strip().lower()
        if level in ['easy', 'intermediate', 'hard']:
            return level
        else:
            print('Invalid choice. Please choose Easy, Intermediate, or Hard.')

def get_time_limit(level):
    """Return the time limit based on difficulty level."""
    if level == 'easy':
        return 0.5
    elif level == 'intermediate':
        return 0.3
    elif level == 'hard':
        return 0.2

print('Fast Draw')
print()
print('Time to test your reflexes and see if you are the fastest')
print('draw in the west!')
print('When you see "DRAW", press Enter as fast as you can.')
print('But you lose if you press Enter before "DRAW" appears.')
print()

# Get difficulty level
difficulty = get_difficulty()
time_limit = get_time_limit(difficulty)

print(f'You selected {difficulty.capitalize()} mode. You have {time_limit} seconds to draw!')
input('Press Enter to begin...')

while True:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()  # Wait for user to press Enter
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # If the player pressed Enter before DRAW! appeared, the input()
        # call returns almost instantly.
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed > time_limit:
        timeElapsed = round(timeElapsed, 4)
        print(f'You took {timeElapsed} seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print(f'You took {timeElapsed} seconds to draw.')
        print('You are the fastest draw in the west! You win!')

    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
