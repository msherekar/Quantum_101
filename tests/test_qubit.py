"""Unit tests for qubit validation and probabilities.
This module verifies normalization checks and experiment counts."""

import unittest
from qubit import Qubit


class TestQubit(unittest.TestCase):
    """Test qubit validation, probabilities, and experiments."""

    def test_valid_qubit_is_normalized(self):
        """Check that valid amplitudes produce normalized probabilities."""
        q = Qubit(0.6, 0.8)
        p0, p1 = q.prob_amplitudes()
        self.assertAlmostEqual(p0 + p1, 1.0, places=9)

    def test_invalid_qubit_raises(self):
        """Check that non-normalized amplitudes raise ValueError."""
        with self.assertRaises(ValueError):
            Qubit(0.5, 0.5)

    def test_experiment_counts_match_shots(self):
        """Ensure measurement counts always sum to requested shots."""
        q = Qubit(1.0, 0.0)
        result = q.experiment(shots=50)
        self.assertEqual(result["zero"] + result["one"], 50)


if __name__ == "__main__":
    unittest.main()
