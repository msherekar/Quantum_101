"""Base class for single-qubit operators.
This module validates gate symbols and enforces an operate contract."""


class SingleQubitOperator:
    """Base class for validated single-qubit gate operators."""

    VALID_OPERATORS = {"H", "X"}

    def __init__(self, oper):
        """Store and validate operator symbol."""
        self.oper = str(oper).strip().upper()
        if self.oper not in self.VALID_OPERATORS:
            raise ValueError(f"Invalid operator: {oper}")

    def operate(self, qubit_vector):
        """Apply this operator to a qubit vector in subclasses."""
        raise NotImplementedError("Subclasses must implement operate().")



