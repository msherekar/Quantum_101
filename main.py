"""
This is the Final exam for course Introduction to Programming Using Python. The script is related to Quantum Computing;
specifically related to states of qubits. It involves 4 other modules - paulix, hadamard, operator and qubit.py.
Script was finished on 12/13/2021.
"""

import numpy as np
import math
from qubit import Qubit
from operators import SingleQubitOperator
from paulix import PauliX
from hadamard import Hadamard

# Read the file contents
with open("qubits.txt", 'rb') as f:  # note it is rb and not just r; file format was different
    contents = f.read()
contents = contents.decode("utf-16").rstrip().split("\n")  # again decoding had to be done in utf-16 and not utf-8

for i in contents:
    i = i.split(" ")  # split by space to get into list format

    # initiate empty lists for 2x1 numpy arrays representing qubits and letter representing Operators
    qubit_list = []
    operators = []

    for j in i:  # for every line in the list
        if j != 'X' and j != 'H' and j != 'f':  # convert the numbers in str format to float
            j = float(j)
            qubit_list.append(j)
        if j == 'X':  # if it is X, instantiate a Paulix object and append
            p = PauliX(j)
            operators.append(p)
        if j == 'H':  # if it is H, instantiate a Hadamard object and append
            h = Hadamard(j)
            operators.append(h)
        else:
            pass

    q = np.array([[qubit_list[0]], [qubit_list[1]]])  # convert numbers  into a numpy array
    qubit = Qubit(q[0][0], q[1][0])  # instantiate an Qubit object to print initial state
    print(qubit.__str__())

    q1 = operators[0].operate(q) # first application of Pauli or Hadamard gate to the qubits

    try:
        q2 = operators[1].operate(q1)   # second application of Pauli or Hadamard gate to the qubits
        PauliX.printout(q2)             # print out
        qubit2 = Qubit(q2[0], q2[1])    # instantiate an object of Qubit by passing new qubit
        print(qubit2.experiment())      # Calculate probabilities

    except IndexError:                  # to take care of missing letter in the line
        pass

    try:
        q3 = operators[2].operate(q2)
        PauliX.printout(q3)
        qubit3 = Qubit(q3[0], q3[1])
        print(qubit3.experiment())
    except IndexError:
        pass

    print(" ")
