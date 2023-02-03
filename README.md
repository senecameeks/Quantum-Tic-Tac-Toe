# Quantum-Tic-Tac-Toe
Create a playable quantum tic tac toe in Cirq

Quantum tic-tac-toe is a two-player game where each player takes turns placing their symbol (X or O) on a 3x3 game board represented by a quantum circuit. The objective of the game is to get three of your symbols in a row (horizontally, vertically, or diagonally) before your opponent.

create_quantum_board function creates a 3x3 grid of qubits, which represent the spaces on the tic-tac-toe board. It then applies a square root of X gate to each qubit, which prepares the qubits for use in the game.

play_quantum_tic_tac_toe function is the main game loop, where players take turns making moves. The player1 and player2 objects should be instances of classes that implement the get_move method. This method is called during each player's turn, and returns a Cirq gate that represents the player's move on the board.

The loop continues for 9 moves (the maximum number of moves in a tic-tac-toe game), and at the end, the circuit is simulated 1024 times to get a distribution of results. The winning conditions are then checked by counting the number of times a particular combination of qubits are in the 1 state, and if any player has achieved three 1s in a row, they are declared the winner. If no player wins, the function returns None.
