import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_initialize_board_creates_empty_board(self):
        """Test that initialize_board function returns an empty 3x3 board."""
        board = Board(3)
        self.assertEqual(board.matrix, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
