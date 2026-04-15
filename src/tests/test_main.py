"""Integration tests for parsing and gate pipeline.
This module validates line parsing and multi-gate application."""

import unittest
from src.main import apply_gates, parse_line


class TestMainPipeline(unittest.TestCase):
    """Test end-to-end parsing and gate application helpers."""

    def test_parse_line(self):
        """Ensure parse_line returns correct amplitudes and gates."""
        qubit, gates = parse_line("1.0 0.0 H X")
        self.assertEqual((qubit.alpha, qubit.beta), (1.0, 0.0))
        self.assertEqual(gates, ["H", "X"])

    def test_apply_two_gates(self):
        """Verify known two-gate pipeline output values."""
        qubit, gates = parse_line("1.0 0.0 H X")
        out = apply_gates(qubit, gates)
        self.assertAlmostEqual(out.alpha, 0.7071067811865475, places=9)
        self.assertAlmostEqual(out.beta, 0.7071067811865475, places=9)

    def test_invalid_gate_raises(self):
        """Confirm unsupported gates raise a validation error."""
        with self.assertRaises(ValueError):
            parse_line("1.0 0.0 H Z")


if __name__ == "__main__":
    unittest.main()
