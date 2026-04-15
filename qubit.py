import numpy as np


class Qubit:
    """
    This class takes in arguments as two floats between 0 and 1 and creates an object representing a qubit.
    Also, object can be checked for validity and authencity (experiment function). Finally, states of the qubit can
    be printed out.
    """
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta


    def validate_amplitudes(self):
        try:
            ((self.alpha * self.alpha) + (self.beta * self.beta)) == 1

        except:
          ((self.alpha * self.alpha) + (self.beta * self.beta)) != 1
          raise Exception("Invalid Amplitude(s)")


    def prob_amplitudes(self):
        return (self.alpha * self.alpha), (self.beta * self.beta)

    def experiment(self):
        p = self.beta * self.beta
        s = np.random.binomial(1, p, 100)
        count = np.bincount(s)
        return f'Percentage of 0 measured: {count[0]}' + "\n" + f'Percentage of 1 measured: {100-count[0]}'


    def __str__(self):
        return f'Initial state: {self.alpha}|0> + {self.beta}|1>'

