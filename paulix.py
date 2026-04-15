"""Pauli-X gate implementation.
This module swaps amplitudes of |0> and |1> components."""

import numpy as np
from operators import SingleQubitOperator


class PauliX(SingleQubitOperator):
    """Implement the Pauli-X gate operation."""

    MATRIX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=float)

    def __init__(self):
        """Initialize a validated Pauli-X operator."""
        super().__init__("X")

    def operate(self, qubit_vector):
        """Apply Pauli-X matrix to the provided qubit vector."""
        return self.MATRIX @ qubit_vector








