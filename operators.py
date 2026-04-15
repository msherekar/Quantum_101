"""Base class for single-qubit operators.
This module validates gate symbols and enforces an operate contract."""


class SingleQubitOperator:
    VALID_OPERATORS = {"H", "X"}

    def __init__(self, oper):
        self.oper = str(oper).strip().upper()
        if self.oper not in self.VALID_OPERATORS:
            raise ValueError(f"Invalid operator: {oper}")

    def operate(self, qubit_vector):
        raise NotImplementedError("Subclasses must implement operate().")



