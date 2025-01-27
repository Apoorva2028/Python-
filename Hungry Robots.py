import random, sys

# Constants:
WIDTH, HEIGHT = 40, 20
NUM_ROBOTS, NUM_TELEPORTS, NUM_WALLS = 10, 2, 100
EMPTY_SPACE, PLAYER, ROBOT, DEAD_ROBOT, WALL = ' ', '@', 'R', 'X', chr(9617)


def main():
    print("Hungry Robots! Escape the robots or trick them into crashing!")
    input("Press Enter to start...")
    board, robots, player = setup_game()

    while True:
        display(board, robots, player)
        if not robots:
            print("You win! All robots destroyed!"); sys.exit()

        player = player_move(board, robots, player)
        robots = move_robots(board, robots, player)

        if player in robots:
            display(board, robots, player)
            print("You were caught! Game over!"); sys.exit()


def setup_game():
    board = {(x, y): EMPTY_SPACE for x in range(WIDTH) for y in range(HEIGHT)}
    for x in range(WIDTH): board[(x, 0)], board[(x, HEIGHT - 1)] = WALL, WALL
    for y in range(HEIGHT): board[(0, y)], board[(WIDTH - 1, y)] = WALL, WALL
    for _ in range(NUM_WALLS): board[get_random_empty(board, [])] = WALL
    robots = [get_random_empty(board, []) for _ in range(NUM_ROBOTS)]
    return board, robots, get_random_empty(board, robots)


def display(board, robots, player):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == player: print(PLAYER, end='')
            elif (x, y) in robots: print(ROBOT, end='')
            else: print(board[(x, y)], end='')
        print()


def player_move(board, robots, player):
    moves = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    while True:
        move = input("Move (WASD or T to teleport): ").upper()  #WASD- UP, LEFT, DOWN, RIGHT
        if move == 'T': return get_random_empty(board, robots)
        if move in moves:
            new_pos = (player[0] + moves[move][0], player[1] + moves[move][1])
            if board.get(new_pos, WALL) != WALL: return new_pos


def move_robots(board, robots, player):
    new_robots = []
    for rx, ry in robots:
        dx, dy = (1 if rx < player[0] else -1 if rx > player[0] else 0,
                  1 if ry < player[1] else -1 if ry > player[1] else 0)
        new_pos = (rx + dx, ry + dy)
        if board.get(new_pos) == WALL: new_pos = (rx, ry)
        if new_pos in new_robots: board[new_pos] = DEAD_ROBOT
        else: new_robots.append(new_pos)
    return [pos for pos in new_robots if board.get(pos) != DEAD_ROBOT]


def get_random_empty(board, robots):
    while True:
        pos = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
        if board[pos] == EMPTY_SPACE and pos not in robots: return pos


if __name__ == '__main__':
    main()

