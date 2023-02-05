import cirq
import random

from player import Player

class QuantumTicTacToe:
    def __init__(self):
        self.board = [cirq.GridQubit(i, j) for i in range(3) for j in range(3)]
        self.current_player = 0
        self.simulator = cirq.Simulator()
        self.circuit = cirq.Circuit()
        self.occupied = {}

    def get_symbol(self):
        return 'X' if self.current_player == 0 else 'O'

    def play_move(self, qubit):
        """Plays the current player's move on the specified qubit.
        Right now this only allows for unitary moves and the measurement gate is immediately appended to the circuit.
        In the future, allow this function to take in 2 qubits and append each qubit to the gate with half probability."""
        symbol = self.get_symbol()
        if symbol == 'X':
            self.circuit.append(cirq.X(qubit))
            self.circuit.append(cirq.measure(qubit))
        elif symbol == 'O':
            self.circuit.append(cirq.Z(qubit))
            self.circuit.append(cirq.measure(qubit))
        self.current_player = (self.current_player + 1) % 2

    def game_over(self):
        """Checks if a winning condition has been met. Or the board is full. Return bool if game is over and the winning symbol or None."""
      
        for i in range(3):
            # Check rows
            if self.occupied.get(str(self.board[i*3])) == self.occupied.get(str((self.board[i*3+1]))) == self.occupied.get(str(self.board[i*3+2])) != None:
                return (True, self.occupied.get(str(self.board[i*3])))
            # Check columns
            if self.occupied.get(str(self.board[i])) == self.occupied.get(str(self.board[i+3])) == self.occupied.get(str(self.board[i+6])) != None:
                return (True, self.occupied.get(str(self.board[i])))

        # Check diagonals
        if self.occupied.get(str(self.board[0])) == self.occupied.get(str(self.board[4])) == self.occupied.get(str(self.board[8])) != None:
            return (True, self.occupied.get(str(self.board[0])))
        if self.occupied.get(str(self.board[2])) == self.occupied.get(str(self.board[4])) == self.occupied.get(str(self.board[6])) != None:
            return (True, self.occupied.get(str(self.board[2])))

        # Check if the board is not full
        if len(self.occupied.keys()) < 9:
            return (False, None) 

        return (True, None)

    def choose_move(self):
        """Chooses a random unoccupied qubit to play the current player's move"""
        result = self.simulator.simulate_moment_steps(self.circuit)
        for res in result:
            self.occupied.update(res.measurements)
        unoccupied_qubits = [qubit for qubit in self.board if str(qubit) not in self.occupied]
        if not unoccupied_qubits:
            return None

        return random.choice(unoccupied_qubits)

def play_quantum_tic_tac_toe(player1, player2):
    qttt = QuantumTicTacToe()
    while True:
        move = qttt.choose_move()
        if move is not None:
            print(move, " : ", qttt.get_symbol())
            qttt.play_move(move)

        # Check if the game has ended
        is_game_over, winner = qttt.game_over()
        if is_game_over:
            return winner

if __name__ == "__main__":
    print("Playing Quantum Tic Tac Toe")
    player1 = Player('X')
    player2 = Player('O')
    winner = play_quantum_tic_tac_toe(player1, player2)
    if winner is not None:
        winner = 'X or Player 1' if winner[0] == 1 else 'O or Player 2'
    print("THE WINNER IS: ", winner)
