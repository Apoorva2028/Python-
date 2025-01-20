import random, sys

print('''Rock, Paper, Scissors
 - Rock beats scissors.
 - Paper beats rock.
 - Scissors beats paper.''')

wins, losses, ties = 0, 0, 0

while True:
    print(f'\n{wins} Wins, {losses} Losses, {ties} Ties')
    player_move = input('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit > ').upper()
    
    if player_move == 'Q':
        print('Thanks for playing!')
        sys.exit()
    
    if player_move not in ('R', 'P', 'S'):
        print('Invalid choice. Type R, P, S, or Q.')
        continue

    moves = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
    player_move = moves[player_move]
    print(' {player_move} versus...')

    computer_move = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
    print(computer_move)

    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif (player_move == 'ROCK' and computer_move == 'SCISSORS') or \
         (player_move == 'PAPER' and computer_move == 'ROCK') or \
         (player_move == 'SCISSORS' and computer_move == 'PAPER'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1
