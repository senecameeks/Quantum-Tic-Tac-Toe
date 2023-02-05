import cirq
import random

"""TODO: Let Player add symbol with half probability to 2 qubits"""
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, circuit, board):
        move = random.choice(board)
        if self.symbol == 'X':
            return cirq.X(move)
        return cirq.Z(move)
