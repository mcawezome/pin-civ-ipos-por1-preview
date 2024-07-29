''''
class Board:
    def __init__(self, grid_size):
        self.empty = " "

    def print_board(self):
'''

class Game:
    def __init__(self, grid_size):
        self.empty = " "
        self.board = [[self.empty] * grid_size] * grid_size
        self.grid_size = grid_size

    def place_move(self):
        """
        Let the user choose which location to place token and validates input
        :return:
            int: The location of move to be made if valid input
        """
        # Validate move placed in this function for the simplicity of program
        while True:
            move = input("Next move for player " + player + " (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8:
                move_int = int(move)
                move_row = int(move_int / self.grid_size)
                move_column = move_int % self.grid_size
                if self.board[move_row][move_column] == self.empty:
                    self.board[move_row][move_column] = self.get_player_token()
                    exit(0)



    def get_player_token(self):
        """
        Chooses the token for the next move
        :return:
            str: The token to be placed for next move
        """
        p1 = "X"
        p2 = "O"
        if self.board.count(self.empty) % 2 == 1:
            return p1
        else:
            return p2

    def is_tie(self):
        """
        Determine if game is tied (assumed game is not won)
        :return:
            bool: True if game is tied
        """
        if self.empty not in self.board:
            return True
        else:
            return False

    def play(self):
        """
        Play the game from start to end
        :return:
        """
        # token = self.get_player_token()
        # while not tied or won
        self.place_move()
