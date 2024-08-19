import unittest

from game import Game

class TestGame(unittest.TestCase):
    def test_is_game_tie(self):
        """
        Test that game correctly identifies tied board
        """
        game = Game(3)
        game.board.matrix = [['O', 'X', 'O'], ['X', 'X', 'O'], ['O', 'O', 'X']]
        self.assertTrue(game.is_game_tie())

    def test_is_game_won(self):
        """
        Test that game correctly identifies won board state
        """
        game = Game(2)
        game.board.matrix = [['O', 'O'], ['X', ' ',]]
        self.assertTrue(game.is_game_won())

    def test_get_player_token(self):
        """
        Test the token the game start with.
        """
        game = Game(3)
        self.assertEqual(game.get_player_token(), 'O')