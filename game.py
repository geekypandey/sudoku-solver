from itertools import product
from pprint import pprint


in_board = lambda x, y: (x >= 0 and x < 9 and y >= 0 and y < 9)  # noqa: E731


def check_row(game, x, y, value):
    if not in_board(x, y):
        raise IndexError('No such board position')
    return all(game[y][i] != value for i in range(9))


def check_column(game, x, y, value):
    if not in_board(x, y):
        raise IndexError('No such board position')
    return all(game[j][x] != value for j in range(9))


def check_square(game, x, y, value):
    if not in_board(x, y):
        raise IndexError('No such board position')
    start_X = (x // 3)*3
    start_Y = (y // 3)*3
    for j in range(start_Y, start_Y + 3):
        for i in range(start_X, start_X + 3):
            if game[j][i] == value:
                return False
    return True


def is_valid(game, x, y, move):
    if check_row(game, x, y, move) and check_column(game, x, y, move) \
            and check_square(game, x, y, move):
        return True
    return False


def solve(game):
    for j, i in product(range(9), range(9)):
        if game[j][i] == 0:
            for move in range(1, 10):
                if is_valid(game, i, j, move):
                    game[j][i] = move
                    solve(game)
                    game[j][i] = 0
            return
    pprint(game)
