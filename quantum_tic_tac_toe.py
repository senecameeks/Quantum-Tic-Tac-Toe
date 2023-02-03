import cirq


def create_quantum_board():
    qubits = [cirq.GridQubit(i, j) for i in range(3) for j in range(3)]
    circuit = cirq.Circuit()
    for q in qubits:
        circuit.append(cirq.X(q)**0.5)
    return circuit, qubits


def play_quantum_tic_tac_toe(player1, player2):
    circuit, qubits = create_quantum_board()

    for i in range(9):
        if i % 2 == 0:
            player = player1
        else:
            player = player2

        move = player.get_move(circuit, qubits)
        circuit.append(move)

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1024)

    winning_boards = [        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for winning_board in winning_boards:
        if (result.histogram(key=lambda x: x[winning_board[0]])['1'] == 1024 and
            result.histogram(key=lambda x: x[winning_board[1]])['1'] == 1024 and
            result.histogram(key=lambda x: x[winning_board[2]])['1'] == 1024):
            return player1.name

    return None
