import numpy as np
import math


class SingleQubitOperator:

    def __init__(self, oper):  # opmat = operator matrix
        self.oper = oper

    def assign_oper(self):
        if self.oper == 'H':
            self.oper = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
        if self.oper == 'X':
            self.oper = np.array([[0, 1], [1, 0]])
        #if self.oper != 'H' or 'X': # for now
            #raise Exception('invalid operator')
        return self.oper



