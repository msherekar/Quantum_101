"""Parse qubit states and apply X/H gate sequences from a text file.
For each input line, print initial state, final state, and sampled measurements."""

import argparse
from pathlib import Path
from hadamard import Hadamard
from paulix import PauliX
from qubit import Qubit

GATE_FACTORY = {"X": PauliX, "H": Hadamard}


def read_input_lines(file_path):
    """Read and return non-empty UTF-16 lines from the input file."""
    raw = Path(file_path).read_bytes()
    text = raw.decode("utf-16")
    return [line.strip() for line in text.splitlines() if line.strip()]


def parse_line(line):
    """Parse one line into a validated qubit instance and gate list."""
    parts = line.split()
    if len(parts) < 3:
        raise ValueError(f"Line must include alpha beta and at least one gate: '{line}'")
    alpha, beta = float(parts[0]), float(parts[1])
    gates = [token.upper() for token in parts[2:]]
    for gate in gates:
        if gate not in GATE_FACTORY:
            raise ValueError(f"Unsupported gate '{gate}' in line: '{line}'")
    return Qubit(alpha, beta), gates


def apply_gates(qubit, gates):
    """Apply gates sequentially and return the final qubit."""
    state = qubit.as_vector()
    for gate in gates:
        state = GATE_FACTORY[gate]().operate(state)
    return Qubit.from_vector(state)


def format_result(initial_qubit, final_qubit, experiment):
    """Format a human-readable output block for one simulation case."""
    p0, p1 = final_qubit.prob_amplitudes()
    return (
        f"Initial state: {initial_qubit}\n"
        f"Final state: {final_qubit}\n"
        f"Final probabilities: P(0)={p0:.6f}, P(1)={p1:.6f}\n"
        f"Measurement ({experiment['shots']} shots): "
        f"0 -> {experiment['zero']}, 1 -> {experiment['one']}"
    )


def parse_args():
    """Parse command-line arguments for input path and shot count."""
    parser = argparse.ArgumentParser(description="Single-qubit gate simulator.")
    parser.add_argument(
        "--input",
        default="qubits.txt",
        help="Relative path to UTF-16 input file with qubit states and gates.",
    )
    parser.add_argument("--shots", type=int, default=100, help="Measurement trials per line.")
    return parser.parse_args()


def main():
    """Run the simulator for each valid line in the input file."""
    args = parse_args()
    lines = read_input_lines(args.input)
    for idx, line in enumerate(lines, start=1):
        try:
            initial_qubit, gates = parse_line(line)
            final_qubit = apply_gates(initial_qubit, gates)
            experiment = final_qubit.experiment(args.shots)
            print(f"Case {idx}")
            print(format_result(initial_qubit, final_qubit, experiment))
        except (ValueError, UnicodeDecodeError) as exc:
            print(f"Case {idx}\nError: {exc}")
        print()


if __name__ == "__main__":
    main()
