import unittest

from src.abstract_game import InvalidMove
from src.tic_tac_toe import TicTacToe


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board_is_empty(self):
        for x in self.game.board:
            self.assertEqual(x, 0)
            self.assertFalse(self.game.is_terminal())
            self.assertFalse(self.game.is_draw())
            self.assertIsNone(self.game.evaluate())

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player, -1)

    def test_valid_move(self):
        for position in range(0, 9):
            with self.subTest(position):
                self.setUp()
                self.game.make_move(position)
                self.assertEqual(self.game.board[position], 1)
                self.assertTrue(self.game.current_player == -1)

    def test_invalid_move(self):
        for position in range(0, 9):
            with self.subTest(position):
                self.setUp()
                self.game.make_move(position)
                self.assertRaises(InvalidMove, self.game.make_move, position)
                self.assertTrue(self.game.current_player == -1) # previous move was invalid -  state should not change

    def test_winning_combinations(self):
        for combination in TicTacToe.winning_combinations:
            with self.subTest(combination=combination):
                self.game = TicTacToe()
                for pos in combination:
                    self.game.board[pos] = 1

                self.assertTrue(self.game.evaluate() == 1)
                self.assertTrue(self.game.is_terminal())
                self.assertFalse(self.game.is_draw())

    def test_draw(self):
        draw_boards = [
            [1, -1, 1,
             -1, 1, -1,
             -1, 1, -1],

            [-1, 1, -1,
             1, -1, 1,
             1, -1, 1],

            [1, -1, 1,
             1, -1, -1,
             -1, 1, -1],

            [-1, 1, -1,
             -1, 1, 1,
             1, -1, 1],

            [1, -1, -1,
             -1, 1, 1,
             1, -1, -1],
        ]

        for board in draw_boards:
            with self.subTest(board=board):
                self.setUp()
                self.game.board = board
                self.assertTrue(self.game.is_draw())


if __name__ == '__main__':
    unittest.main()
