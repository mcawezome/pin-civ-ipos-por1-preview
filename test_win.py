# This is not suitable for board on n dimensions. Redone
# Use unit test not pytest
import unittest

empty = " "
grid_size = 3
board = [[empty]*grid_size]*grid_size
def is_game_won():
    n = len(board)
    is_won = False
    for i in range(n):
        #check horizontal wins
        if all(board[i][j] == board[i][0] != empty for j in range(n)):
            is_won = True
        # check vertical wins
        elif all(board[i][j] == board[0][j] != empty for j in range(n)):
            is_won = True
        # check L->R diagonal wins
        elif all(board[i][i] == board[0][0] != empty for i in range(n)):
            is_won = True
        # check R -> L diagonal wins
        elif all(board[n-1-i] == board[0][n-1] != empty for i in range(n)):
            is_won = True
    return is_won


