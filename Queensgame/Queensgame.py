BOARD_SIZE = 8
DIMENSION = (BOARD_SIZE, BOARD_SIZE)
QUEEN_CHAR = '*'

def createboard():
    return [ list(input()) for _ in range(BOARD_SIZE)]
def can_capture(board, y, x):
    return can_hit(board, y, x, 1, 0) or can_hit(board, y, x, -1, 0) or can_hit(board, y, x, 0, 1) or can_hit(board, y, x, 0, -1)\
        or can_hit(board, y, x, 1, 1) or can_hit(board, y, x, -1, -1) or can_hit(board, y, x, -1, 1) or can_hit(board, y, x, 1, -1)
def can_hit(board, y, x, dir_y, dir_x):
    _y, _x = y + dir_y, x + dir_x
    while 0 <= _y <= BOARD_SIZE -1 and 0 <= _x <= BOARD_SIZE -1:
        if board[_y][_x] == QUEEN_CHAR:
            return True
        _y += dir_y
        _x += dir_x
    return False
def is_solvable(board):
    queen_count = 0
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == QUEEN_CHAR:
                queen_count+=1
                if can_capture(board, y, x):
                    return False
    return queen_count == BOARD_SIZE
def main():
    print("valid") if is_solvable(createboard()) else print("invalid")
if __name__ == "__main__":
    main()