import Board as b
class Game:
    def __init__(self, grid_size):
        self.empty = " "
        self.board = b.Board(grid_size)
        # self.board = [[self.empty] * grid_size] * grid_size

    def place_move(self):
        """
        Let the user choose which location to place token and validates input
        :return:
            int: The location of move to be made if valid input
        """
        # Validate move placed in this function for the simplicity of program
        while True:
            move = input("Next move for player " + self.get_player_token() + " (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8:
                move_int = int(move)
                move_row = int(move_int / self.board.grid_size)
                move_column = move_int % self.board.grid_size
                if self.board.matrix[move_row][move_column] == self.empty:
                    self.board.matrix[move_row][move_column] = self.get_player_token()
                    break



    def get_player_token(self):
        """
        Chooses the token for the next move
        :return:
            str: The token to be placed for next move
        """
        p1 = "X"
        p2 = "O"
        if self.board.matrix.count(self.empty) % 2 == 1:
            return p1
        else:
            return p2

    def is_game_won(self):
        n = len(self.board.matrix)
        board = self.board.matrix
        empty = self.board.empty
        is_won = False
        for i in range(n):
            # check horizontal wins
            if all(board[i][j] == board[i][0] != empty for j in range(n)):
                is_won = True
            # check vertical wins
            elif all(board[i][j] == board[0][j] != empty for j in range(n)):
                is_won = True
            # check L->R diagonal wins
            elif all(board[i][i] == board[0][0] != empty for i in range(n)):
                is_won = True
            # check R -> L diagonal wins
            elif all(board[n - 1 - i] == board[0][n - 1] != empty for i in range(n)):
                is_won = True
        return is_won

    def is_game_tie(self):
        """
        Determine if game is tied (assumed game is not won)
        :return:
            bool: True if game is tied
        """
        for row in self.board.matrix:
            if self.board.empty in row:
                return False
        return False

    def play(self):
        """
        Play the game from start to end
        :return:
        """
        # token = self.get_player_token()
        # while not tied or won
        game_over = False
        winner = "No one"
        while game_over == False:
            self.place_move()
            self.board.print_board()
            if self.is_game_won():
                game_over = True
                winner = self.get_player_token()
            elif self.is_game_tie():
                game_over = True
        print(winner, " won the game!")
