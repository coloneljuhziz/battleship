from enum import Enum

board = []

class Cell(object):
    class States(Enum):
        EMPTY = 0
        MISSED = 1
        HIT = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = self.States.EMPTY
        self.is_ship = False

    def __repr__(self):
        if self.state == self.States.EMPTY:
            return '   |'
        elif self.state == self.States.MISSED:
            return ' · |'
        elif self.state == self.States.HIT:
            return ' X |'
        else:
            return ' ? |'


class Ship(Cell):
    def __init__(self, user, parts):
        self.user = user
        self.sunk = False
        self.parts = None

    def check_ship_sunk(self):
        return None

    @classmethod
    def create_ship(cls):
        user = 'Player1'
        sunk = False
        parts = get_ship_coords()


def render_board():
    for row in board:
        print('|', end='')
        for col in row:
            print(col, end='')
        print()


def get_ship_coords():
    print('Player1, input ship coords (horizontal then vertical), axis (h/v), size (2,2,h,3): ', end='')

    while True:
        pre_coords = input()
        coords = pre_coords.split(',')
        x, y, axis, size = tuple(coords)
        x = int(y) - 1
        y = int(y) - 1
        axis = axis.strip()
        size = int(size)
        if x > 10 or y > 10 or x < 0 or y < 0:
            print('Wrong coordinates! Try again!')
        elif axis == 'h' and (x + size) > 10:
            print('Ship out of board! Try again!')
        elif axis == 'v' and (y + size) > 10:
            print('Ship out of board! Try again!')
        else:
            print('Ship added!')
            break

    res = []

    for _ in range(size):
        res.append((x, y))
        if axis == 'h':
            x += 1
        else:
            y += 1

    return res


def fire(x,y):
    c = board[y][x]
    if c.is_ship:
        c.state = Cell.States.HIT
    else:
        c.state = Cell.States.MISSED
    # render_board()

def main():
    for i in range(10):
        board_row = []
        board.append(board_row)
        for j in range(10):
            live_cell = Cell(i, j)
            board_row.append(live_cell)

    res = get_ship_coords()
    print(res)

    for pair in res:
        x,y = pair
        c = board[y][x]
        c.is_ship = True

    fire(4,4)
    for x in range(0,10):
        for y in range(0,10):
            fire(x,y)

    render_board()


main()
