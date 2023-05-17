from setup import TicTacToeGame, TicTacToeBoard
import unittest
from unittest.mock import patch
import sqlite3
import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

connection = sqlite3.connect(r'test_database.db')
cursor = connection.cursor()

class TestClass(unittest.TestCase):
    def setUp(self):
        self.tictactoegame = TicTacToeGame()
        self.tictactoeboard = TicTacToeBoard(self.tictactoegame)

    def test_reset_board(self):
        self.tictactoegame._has_winner = True
        self.assertEqual(self.tictactoegame._has_winner, True)
        self.tictactoeboard.reset_board()
        self.assertEqual(self.tictactoegame._has_winner, False)

    #@patch('tic_tac_toe.Button')
    def test_play(self):
        self.tictactoegame._has_winner = True
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.position = (50, 70)
        '''
        m = PyMouse()
        m.position() #gets mouse current position coordinates
        m.move(x,y)
        m.click(x,y,1) #the third argument "1" represents the mouse button
        m.press(x,y) #mouse button press
        m.release(x,y) #mouse button release
        '''
        self.tictactoeboard.play(mouse.click(Button.left, 1))

if __name__ == '__main__':
    unittest.main()
