#print_board
grid_size = 3
empty = " "
board = [[empty]*grid_size]*grid_size
for row in board:
    for n_column, column in enumerate(board):
        print(column, end="")
        if n_column < grid_size-1:
            print("|", end="")
    print()
    print("---------")

