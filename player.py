import cirq
import random

class RandomPlayer:
    def get_move(self, circuit, board, symbol):
        move = random.choice(board)
        if symbol == 'X':
            return cirq.X(move)
        return cirq.Z(move)
