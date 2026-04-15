"""Qubit data model and measurement helpers.
This module validates amplitudes and provides probability/sampling methods."""

import math, numpy as np

TOLERANCE = 1e-9


class Qubit:
    def __init__(self, alpha, beta):
        self.alpha = float(alpha)
        self.beta = float(beta)
        self.validate_amplitudes()

    def validate_amplitudes(self):
        norm = (self.alpha ** 2) + (self.beta ** 2)
        if not math.isclose(norm, 1.0, rel_tol=0.0, abs_tol=TOLERANCE):
            raise ValueError(f"Invalid amplitudes: alpha^2 + beta^2 = {norm}")

    def prob_amplitudes(self):
        return (self.alpha ** 2), (self.beta ** 2)

    def experiment(self, shots=100):
        _, p1 = self.prob_amplitudes()
        samples = np.random.binomial(1, p1, shots)
        count = np.bincount(samples, minlength=2)
        return {"shots": shots, "zero": int(count[0]), "one": int(count[1])}

    def as_vector(self):
        return np.array([[self.alpha], [self.beta]], dtype=float)

    @classmethod
    def from_vector(cls, vector):
        return cls(float(vector[0][0]), float(vector[1][0]))

    def __str__(self):
        return f"{self.alpha}|0> + {self.beta}|1>"

