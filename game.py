from pprint import pprint


def check_row(game, x, y, value):
    if not (x >= 0 and y >= 0 and x < 9 and y < 9):
        raise IndexError('No such board position')
    for i in range(9):
        if game[y][i] == value:
            return False
    else:
        return True


def check_column(game, x, y, value):
    if not (x >= 0 and y >= 0 and x < 9 and y < 9):
        raise IndexError('No such board position')
    for j in range(9):
        if game[j][x] == value:
            return False
    else:
        return True


def check_square(game, x, y, value):
    if not (x >= 0 and y >= 0 and x < 9 and y < 9):
        raise IndexError('No such board position')
    start_X = (x // 3)*3
    start_Y = (y // 3)*3
    for j in range(start_Y, start_Y + 3):
        for i in range(start_X, start_X + 3):
            if game[j][i] == value:
                return False
    else:
        return True


def is_valid(game, x, y, move):
    if check_row(game, x, y, move) and check_column(game, x, y, move) \
            and check_square(game, x, y, move):
        return True
    else:
        return False


def solve(game):
    for j in range(9):
        for i in range(9):
            if game[j][i] == 0:
                for move in range(1, 10):
                    if is_valid(game, i, j, move):
                        game[j][i] = move
                        solve(game)
                        game[j][i] = 0
                return
    pprint(game)
