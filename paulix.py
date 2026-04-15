import numpy as np
import math
from operators import SingleQubitOperator

class PauliX(SingleQubitOperator):
    """
    This class is a derivative of Single Qubit Operator. Argument is a 2x1 array to which the operate function applies
    the Paulix gate and printout function prints final state
    """
    def __init__(self, qubit):
        super().__init__(qubit)


    def operate(self, qubit):
        x = np.array([[0, 1], [1, 0]]) # array representing paulix gate
        new_qubit = np.matmul(x, qubit)
        return new_qubit

    def printout(new_qubit):
        print (f'Final state: {new_qubit[0][0]}|0> + {new_qubit[1][0]}|1>')








