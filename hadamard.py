"""Hadamard gate implementation.
This module creates and applies equal superposition transforms."""

import math, numpy as np
from operators import SingleQubitOperator


class Hadamard(SingleQubitOperator):
    """Implement the Hadamard gate operation."""

    MATRIX = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=float) / math.sqrt(2)

    def __init__(self):
        """Initialize a validated Hadamard operator."""
        super().__init__("H")

    def operate(self, qubit_vector):
        """Apply Hadamard matrix to the provided qubit vector."""
        return self.MATRIX @ qubit_vector


