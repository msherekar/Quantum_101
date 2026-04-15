import numpy as np
import math
import warnings


class SingleQubitOperator:
    """
    This class accepts letter H or X as in argument and creates an instance variable . X represents Paulix gate
    and H represents Hadamard gate. It is supposed to raise an exception when the any other letter is passed as an
    argument.
    """
    def __init__(self, oper: str):
        self.oper = oper
        if self.oper != 'H' and self.oper != 'X':
            raise Exception('Invalid operator.')



