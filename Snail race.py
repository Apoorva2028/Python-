import random, time, sys

# Constants
MAX_NUM_SNAILS = 8
FINISH_LINE = 40

print('''Snail Race 🐌
    @v <-- snail
''')

# Get the number of snails
while True:
    numSnails = input(f'How many snails will race? (2-{MAX_NUM_SNAILS}): ')
    if numSnails.isdigit() and 2 <= int(numSnails) <= MAX_NUM_SNAILS:
        numSnails = int(numSnails)
        break
    print(f'Enter a number between 2 and {MAX_NUM_SNAILS}.')

# Get snail names
snailNames = []
for i in range(numSnails):
    while True:
        name = input(f'Enter snail #{i + 1}\'s name: ')
        if name and name not in snailNames:
            snailNames.append(name[:20])  # Limit name length to 20
            break
        print('Invalid or duplicate name. Try again.')

# Initialize snail positions
snailProgress = {name: 0 for name in snailNames}

# Start the race
print('\n' * 40)
print('START' + ' ' * (FINISH_LINE - 5) + 'FINISH')
time.sleep(1.5)

while True:
    for _ in range(random.randint(1, numSnails // 2)):
        snail = random.choice(snailNames)
        snailProgress[snail] += 1

        if snailProgress[snail] >= FINISH_LINE:
            print(f'{snail} wins the race!')
            sys.exit()

    # Clear the screen
    print('\n' * 40)
    print('START' + ' ' * (FINISH_LINE - 5) + 'FINISH')

    # Display the snails
    for name in snailNames:
        progress = snailProgress[name]
        print(' ' * progress + name)
        print('.' * progress + '@v')

    time.sleep(0.5)
