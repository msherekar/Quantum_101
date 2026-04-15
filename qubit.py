"""Qubit data model and measurement helpers.
This module validates amplitudes and provides probability/sampling methods."""

import math, numpy as np

TOLERANCE = 1e-9


class Qubit:
    """Represent a normalized single qubit with utility operations."""

    def __init__(self, alpha, beta):
        """Create a qubit from amplitudes and validate normalization."""
        self.alpha = float(alpha)
        self.beta = float(beta)
        self.validate_amplitudes()

    def validate_amplitudes(self):
        """Raise ValueError when amplitudes are not properly normalized."""
        norm = (self.alpha ** 2) + (self.beta ** 2)
        if not math.isclose(norm, 1.0, rel_tol=0.0, abs_tol=TOLERANCE):
            raise ValueError(f"Invalid amplitudes: alpha^2 + beta^2 = {norm}")

    def prob_amplitudes(self):
        """Return probabilities of measuring states |0> and |1>."""
        return (self.alpha ** 2), (self.beta ** 2)

    def experiment(self, shots=100):
        """Simulate repeated measurements and return outcome counts."""
        _, p1 = self.prob_amplitudes()
        samples = np.random.binomial(1, p1, shots)
        count = np.bincount(samples, minlength=2)
        return {"shots": shots, "zero": int(count[0]), "one": int(count[1])}

    def as_vector(self):
        """Return the qubit as a 2x1 NumPy column vector."""
        return np.array([[self.alpha], [self.beta]], dtype=float)

    @classmethod
    def from_vector(cls, vector):
        """Build a qubit from a 2x1 NumPy column vector."""
        return cls(float(vector[0][0]), float(vector[1][0]))

    def __str__(self):
        """Return Dirac notation-like text for the qubit state."""
        return f"{self.alpha}|0> + {self.beta}|1>"

