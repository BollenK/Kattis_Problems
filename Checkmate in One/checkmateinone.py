BOARD_SIZE = 8
P_KING_CHAR = "K"
P_GUARDED_KING_CHAR = "Q"
P_GUARDED_ROOK_CHAR = "W"
P_ROOK_CHAR = "R"
KING_CHAR = "k"
CHECK_CHAR = "C"
GUARDED_CHAR = "X"
import copy

KING_GUARD = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
ROOK_GUARD = [(1,0), (0,1), (-1,0), (0,-1)]
def createboard():
    return [ list(input()) for _ in range(BOARD_SIZE)]
def print_board(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            print(board[y][x], end="")
        print()
def mark_guarded_sqaures(board):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == P_KING_CHAR or board[y][x] == P_GUARDED_KING_CHAR:
                for _y, _x in KING_GUARD:
                    if 0 <= y + _y <= BOARD_SIZE -1 and 0 <= x + _x <= BOARD_SIZE -1 and board[y + _y][x + _x] != KING_CHAR:
                        if board[y + _y][x + _x] == P_ROOK_CHAR:
                            board[y + _y][x + _x] = P_GUARDED_ROOK_CHAR
                        else:
                            board[y + _y][x + _x] = GUARDED_CHAR
                # markt all surrounding spots till collision.
            elif board[y][x] == P_ROOK_CHAR or board[y][x] == P_GUARDED_ROOK_CHAR:
                for _y, _x in ROOK_GUARD:
                    new_y, new_x = y + _y, x + _x
                    while 0 <= new_y <= BOARD_SIZE -1 and 0 <= new_x <= BOARD_SIZE -1 and board[new_y][new_x] != P_KING_CHAR:
                        if not board[new_y][new_x] == KING_CHAR and not board[new_y][new_x] == CHECK_CHAR:
                            if board[new_y][new_x] == P_KING_CHAR:
                                board[new_y][new_x] = P_GUARDED_KING_CHAR
                            else:
                                board[new_y][new_x] = GUARDED_CHAR
                        else:
                            board[new_y][new_x] = CHECK_CHAR
                        new_y+=_y
                        new_x+=_x
    return board
                # Mark all horizontal and vertical squares untill collision.
def can_king_escape(board):
    rcc = False
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[y][x] == CHECK_CHAR:
                rcc = True
                # print("skjdfnskjdfsdkfhskdjf")
                for _y, _x in KING_GUARD:
                    if 0 <= y + _y <= BOARD_SIZE -1 and 0 <= x + _x <= BOARD_SIZE -1 and not board[y + _y][x + _x] in [P_GUARDED_KING_CHAR, P_GUARDED_ROOK_CHAR, GUARDED_CHAR]:
                        return True
                
    return not rcc
def check_moves(board, y, x):
    if board[y][x] == P_GUARDED_ROOK_CHAR or board[y][x] == P_ROOK_CHAR:
        for _y, _x in ROOK_GUARD:
            new_board = copy.deepcopy(board)
            # print(f"Rook guard: ({_y}, {_x})")
            # print()
            new_y, new_x = y + _y, x + _x
            while 0 <= new_y <= BOARD_SIZE -1 and 0 <= new_x <= BOARD_SIZE -1 and board[new_y][new_x] != P_KING_CHAR:
                new_board[new_y - _y][new_x - _x] = "."
                new_board[new_y][new_x] = "R"
                # print(new_x - _x)
                # print()
                # print("pre-mark:")
                # print_board(new_board)
                # print()
                # print("post mark:")
                marked_board = mark_guarded_sqaures(copy.deepcopy(new_board))
                # print_board(marked_board)
                # print()
                if not can_king_escape(marked_board):
                    return True
                new_y+=_y
                new_x+=_x
            # print()
    return False

def main():
    board = createboard()
    tb = copy.deepcopy(board)
    # if not can_king_escape(tb):
    #     print("Yes")
    #     return
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            b = board
            tb = copy.deepcopy(b)
            tb = mark_guarded_sqaures(tb)
            # print_board(tb)
            if check_moves(b, y, x):
                print("Yes")
                return


            
    print("No")
if __name__ == "__main__":
    main()