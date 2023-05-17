import unittest
from unittest.mock import MagicMock, Mock, patch
from tic_tac_toe import Player, TicTacToeGame

class TestClass(unittest.TestCase):
    def setUp(self):
        self.tictactoegame = TicTacToeGame()

    def test_combos(self):
        self.assertEqual(self.tictactoegame._get_winning_combos(), 
                         [[(0, 0), (0, 1), (0, 2)],
                          [(1, 0), (1, 1), (1, 2)],
                          [(2, 0), (2, 1), (2, 2)],
                          [(0, 0), (1, 0), (2, 0)],
                          [(0, 1), (1, 1), (2, 1)],
                          [(0, 2), (1, 2), (2, 2)],
                          [(0, 0), (1, 1), (2, 2)],
                          [(0, 2), (1, 1), (2, 0)]])
        
        self.assertNotEqual(self.tictactoegame._get_winning_combos(), 0)

    def test_has_winner(self):
        self.assertEqual(self.tictactoegame.has_winner(), False)
        self.tictactoegame._has_winner = True
        self.assertEqual(self.tictactoegame.has_winner(), True)
        self.assertNotEqual(self.tictactoegame.has_winner(), False)

    @patch('tic_tac_toe.all')
    def test_is_tied(self, mock_all):
        self.tictactoegame._has_winner = True
        mock_all.return_value = False
        self.assertEqual(self.tictactoegame.is_tied(), False)

        self.tictactoegame._has_winner = False
        mock_all.return_value = True
        self.assertEqual(self.tictactoegame.is_tied(), True)
    
    @patch('tic_tac_toe.Move')
    def test_is_valid_move(self, move_mock):
        move = move_mock(0, 0, "X")
        self.assertEqual(self.tictactoegame.is_valid_move(move), True)
        self.tictactoegame._has_winner = True
        self.assertEqual(self.tictactoegame.is_valid_move(move), False)

    def test_reset(self):
        self.tictactoegame._has_winner = True
        self.assertEqual(self.tictactoegame._has_winner, True)
        self.tictactoegame.reset_game()
        self.assertEqual(self.tictactoegame._has_winner, False)

    def test_toggle_player(self):
        self.assertEqual(self.tictactoegame.current_player, Player(label='X', color='blue'))
        self.assertNotEqual(self.tictactoegame.current_player, Player(label="O", color="green"))
        self.tictactoegame.toggle_player()
        self.assertNotEqual(self.tictactoegame.current_player, Player(label='X', color='blue'))
        self.assertEqual(self.tictactoegame.current_player, Player(label="O", color="green"))
    

if __name__ == '__main__':
    unittest.main()