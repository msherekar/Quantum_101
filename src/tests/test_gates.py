"""Unit tests for single-qubit gate behavior.
This module checks known basis/superposition transformations."""

import math, unittest
from src.hadamard import Hadamard
from src.paulix import PauliX
from src.qubit import Qubit


class TestGates(unittest.TestCase):
    """Test known basis-state behavior for supported gates."""

    def test_pauli_x_on_zero(self):
        """Confirm X|0> transforms to |1>."""
        q = Qubit(1.0, 0.0)
        out = PauliX().operate(q.as_vector())
        result = Qubit.from_vector(out)
        self.assertAlmostEqual(result.alpha, 0.0, places=9)
        self.assertAlmostEqual(result.beta, 1.0, places=9)

    def test_hadamard_on_zero(self):
        """Confirm H|0> transforms to equal superposition."""
        q = Qubit(1.0, 0.0)
        out = Hadamard().operate(q.as_vector())
        result = Qubit.from_vector(out)
        expected = 1.0 / math.sqrt(2)
        self.assertAlmostEqual(result.alpha, expected, places=9)
        self.assertAlmostEqual(result.beta, expected, places=9)


if __name__ == "__main__":
    unittest.main()
