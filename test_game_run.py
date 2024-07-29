'''
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            board[int(move)] = player
            break
        else:
            print("Invalid move, try again.")
'''

def valid_move(move, board):
    move = input("Next move for player " + player + " (0-8): ")
    if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
        return True
    return False

p1 = "X"
p2 = "O"
empty = " "
grid_size = 3
board = [[empty*grid_size]*grid_size]
while True:
    player = p1 if board.count(empty) % 2 == 1 else p2
    move = input("Next move for player " + player + " (0-8): ")
    if(valid_move(move, board)):
        move_int = int(move)
        move_row = int(move_int / grid_size)
        move_column = move_int % grid_size
        board[move_row][move_column] = player
    else:
        print("Invalid Move")



