import numpy as np
import math
import warnings

with warnings.catch_warnings():
    warnings.simplefilter(action='ignore', category=FutureWarning)
class SingleQubitOperator:
    def __init__(self, oper: str):
        self.oper = oper
        try:
            self.oper == 'H' and self.oper == 'X'
        except:
            raise Exception("Invalid Operator")











