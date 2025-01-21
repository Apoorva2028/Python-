import sys

print('''Fibonacci Sequence
The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. Example: 0, 1, 1, 2, 3, 5, 8...
''')

while True:
    response = input('Enter the Nth Fibonacci number to calculate (or QUIT to exit): ').strip().upper()
    
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    if not response.isdigit() or int(response) <= 0:
        print('Please enter a positive number or QUIT.')
        continue

    nth = int(response)
    if nth == 1:
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('The #2 Fibonacci number is 1.')
        continue

    if nth >= 10000:
        print('WARNING: Large input may take time. Press Ctrl+C to stop.')
        input('Press Enter to continue...')

    # Calculate Fibonacci sequence
    a, b = 0, 1
    print('0, 1', end='')
    for i in range(3, nth + 1):
        a, b = b, a + b
        print(f', {b}', end='')

    print(f'\n\nThe #{nth} Fibonacci number is {b}.')
