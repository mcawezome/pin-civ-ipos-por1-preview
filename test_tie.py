empty = " "
grid_size = 3
board = [[empty]*grid_size]*grid_size

def is_tie(board):
    if empty not in board:
        print("It's a tie!")
        return True
    else:
        return False