# Quantum 101 - Single Qubit Gate Simulator

This project simulates a single qubit by reading initial amplitudes and a sequence of gates from an input file.
For each case, the program validates the qubit, applies gates in order, and reports final state + measurement results.

This project is a very good beginner bridge between programming and quantum computing fundamentals, and it matters because it teaches the core qubit model: a qubit is not just 0/1, but amplitudes alpha and beta with normalization. It also teaches gates as linear algebra, where X and H are matrix operations on state vectors, exactly how real quantum circuits are mathematically modeled, and it builds intuition for quantum programs by showing sequential circuit behavior through multiple gate applications in order. It connects theory to measurement by using probabilities P(0) and P(1) plus repeated sampling (shots) to show how quantum states become classical outcomes, and it reinforces validation discipline by rejecting invalid amplitudes and gates, similar to real quantum SDK constraints. For beginners, this gives comfort with Dirac notation versus vector notation (a|0> + b|1> <-> column vector), understanding that measurement is probabilistic rather than deterministic, and awareness that gate order matters because quantum operations are not generally interchangeable. It also provides early exposure to simulation workflow before moving to frameworks like Qiskit, Cirq, or PennyLane, while building software engineering habits for quantum code such as modular gate design, parsing, testing, CLI usage, and reproducible environments with uv. This is a strong starting project because you already implemented the same conceptual pipeline used in larger quantum tools: input circuit -> build state -> apply gate operators -> compute probabilities -> sample measurements, which is essentially the hello-world architecture of quantum simulation. Once this foundation is solid, the natural next step is to extend from one qubit to two qubits (tensor products, CNOT, and entanglement), where real quantum behavior becomes much more interesting; from there, you can grow this into a mini portfolio-ready quantum simulator project.

## Features

- Supports single-qubit gates: `H` (Hadamard) and `X` (Pauli-X)
- Validates input amplitudes (`alpha^2 + beta^2 = 1`)
- Computes final probabilities `P(0)` and `P(1)`
- Runs measurement simulation using configurable shot count
- Includes unit and integration tests

## Project Structure

- `src/main.py` - CLI entrypoint, file parsing, gate application pipeline, output formatting
- `src/qubit.py` - qubit model, normalization validation, probability and measurement helpers
- `src/operators.py` - base operator contract and validation
- `src/paulix.py` - Pauli-X gate matrix implementation
- `src/hadamard.py` - Hadamard gate matrix implementation
- `src/tests/` - test suite (`test_qubit.py`, `test_gates.py`, `test_main.py`)
- `qubits.txt` - sample UTF-16 input file
- `scripts/` - git workflow helper scripts
- `archive/` - older prototype scripts retained for reference

## Requirements

- Python `>=3.9`
- `uv` package manager

## Setup (uv)

```bash
uv venv
uv sync
```

Run commands using `uv run` so they execute inside the project environment.

## Usage

Default run:

```bash
uv run python -m src.main
```

Custom input file and shots:

```bash
uv run python -m src.main --input qubits.txt --shots 200
```

## Input File Format

Each non-empty line must follow:

```text
alpha beta gate1 gate2 gate3 ...
```

- `alpha` and `beta` are floating-point amplitudes
- Gates are uppercase tokens from: `X`, `H`
- Example:

```text
1.0 0.0 H X H
0.0 1.0 X H
```

## Output

For each case, the program prints:

- Initial state
- Final state after all gates
- Final probabilities: `P(0)`, `P(1)`
- Measurement counts for the given number of shots

## Running Tests

```bash
uv run python -m unittest discover -s src/tests -v
```

## Notes

- Input file is decoded as UTF-16 to match the provided dataset.
- Invalid gates or invalid amplitudes raise clear errors per case.
