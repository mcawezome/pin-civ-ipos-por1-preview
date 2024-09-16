class Board:
    def __init__(self, grid_size):
        self.empty = " "
        self.grid_size = grid_size
        # self.matrix = [[self.empty] *3] * 3] This does not fly, due to unknown bug
        self.matrix = self.matrix = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_board(self):
        """
        prints a command line representation of the game board.
        """
        for row in self.matrix:
            for n_column, column in enumerate(self.matrix):
                print(row[n_column], end="")
                if n_column < self.grid_size - 1:
                    print("|", end="")
            print()
            print("---------")

    def place_move(self,row,col, token):
        """
        places a move at a given row, column for a specified token.
        :param row: row coordinate for the token to change
        :param col: column coordinate for the token to change
        :param token: 'O' or 'X', token to change
        """
        self.matrix[row][col] = token
