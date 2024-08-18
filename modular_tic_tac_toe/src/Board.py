class Board:
    def __init__(self, grid_size):
        self.empty = " "
        self.grid_size = grid_size
        self.matrix = self.matrix = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def print_board(self):
        for row in self.matrix:
            for n_column, column in enumerate(self.matrix):
                print(row[n_column], end="")
                if n_column < self.grid_size - 1:
                    print("|", end="")
            print()
            print("---------")

    def place_move(self,row,col, token):
        self.matrix[row][col] = token

#    def generate_win_cons(self):