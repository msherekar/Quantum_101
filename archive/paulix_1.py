import numpy as np
import math
from operator2 import SingleQubitOperator


class PauliX(SingleQubitOperator):
    x = np.array([[0, 1], [1, 0]])

    def __init__(self, qubit):
        super().__init__(qubit)


    def operate(self, qubit):  # where will the qubit come from?
        x = np.array([[0, 1], [1, 0]])
        self = np.matmul(x, qubit)
        return self

q = np.array([[1], [0]]) # qubit

j1 = PauliX('X') # instance of PauliX
print(j1.operate(q))
