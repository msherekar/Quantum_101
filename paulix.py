"""Pauli-X gate implementation.
This module swaps amplitudes of |0> and |1> components."""

import numpy as np
from operators import SingleQubitOperator


class PauliX(SingleQubitOperator):
    MATRIX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=float)

    def __init__(self):
        super().__init__("X")

    def operate(self, qubit_vector):
        return self.MATRIX @ qubit_vector








