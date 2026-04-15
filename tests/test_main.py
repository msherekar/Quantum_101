"""Integration tests for parsing and gate pipeline.
This module validates line parsing and multi-gate application."""

import unittest
from main import apply_gates, parse_line


class TestMainPipeline(unittest.TestCase):
    def test_parse_line(self):
        qubit, gates = parse_line("1.0 0.0 H X")
        self.assertEqual((qubit.alpha, qubit.beta), (1.0, 0.0))
        self.assertEqual(gates, ["H", "X"])

    def test_apply_two_gates(self):
        qubit, gates = parse_line("1.0 0.0 H X")
        out = apply_gates(qubit, gates)
        self.assertAlmostEqual(out.alpha, 0.7071067811865475, places=9)
        self.assertAlmostEqual(out.beta, 0.7071067811865475, places=9)

    def test_invalid_gate_raises(self):
        with self.assertRaises(ValueError):
            parse_line("1.0 0.0 H Z")


if __name__ == "__main__":
    unittest.main()
