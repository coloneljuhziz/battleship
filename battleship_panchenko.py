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


def render_board():
    for row in board:
        print('|', end='')
        for col in row:
            print(col, end='')
        print()


def get_ship_coords(a=None):
    if a is None:
        print('Player1, input ship coords, axis (h/v), size (2,2,h,3): ', end='')
        pre_coords = input()
    else:
        pre_coords = a

    coords = pre_coords.split(',')
    x, y, axis, size = tuple(coords)
    x = int(x)
    y = int(y)
    axis = axis.strip()
    size = int(size)

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

    res = get_ship_coords('3,4,h,3')
    print(res)

    for pair in res:
        x,y = pair
        c = board[y][x]
        c.is_ship = True

    render_board()
    fire(4,4)
    for x in range(0,10):
        for y in range(0,10):
            fire(x,y)

    render_board()


main()
