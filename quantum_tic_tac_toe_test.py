import unittest
import cirq
import random
from quantum_tic_tac_toe import *
from player import Player

class TestQuantumTicTacToe(unittest.TestCase):
	def test_get_symbol(self):
		# Test that the get_symbol method returns 'X' for the first player
		# and 'O' for the second player
		qttt = QuantumTicTacToe()
		self.assertEqual(qttt.get_symbol(), 'X')
		qttt.current_player = 1
		self.assertEqual(qttt.get_symbol(), 'O')

	def test_create_quantum_board(self):
		qttt = QuantumTicTacToe()
		self.assertEqual(len(qttt.board), 9, "Board should have 9 qubits")
		for qubit in qttt.board:
			assert isinstance(qubit, cirq.GridQubit), "Each element in board should be a Qubit"

	def test_play_quantum_tic_tac_toe(self):
		player1 = Player('X')
		player2 = Player('O')
		result = play_quantum_tic_tac_toe(player1, player2)
		assert result is None or result in ([0], [1]), "Result should be None or 0 or 1"

if __name__ == '__main__':
    unittest.main()
