import numpy as np
import math
from qubit_1 import Qubit
from operator2 import SingleQubitOperator
from paulix import PauliX
from hadamard import Hadamard

# Read the file contents (Done)
with open("qubits.txt", 'rb') as f:
    contents = f.read()
contents = contents.decode("utf-16").rstrip().split("\n")

for i in contents:
    i = i.split(" ")
    qubit_list = []
    operators = []

    for j in i:
        if j != 'X' and j != 'H' and j != 'f':
            j = float(j)
            qubit_list.append(j)
        if j == 'X':
            p = PauliX(j)
            operators.append(p)
        if j == 'H':
            h = Hadamard(j)
            operators.append(h)
        else:
            pass

    q = np.array([[qubit_list[0]], [qubit_list[1]]])
    qubit = Qubit(q[0], q[1])
    print(qubit.__str__())

    q1_list = []
    q1 = operators[0].operate(q)
    qubit1 = Qubit(q1[0], q1[1])
    print(qubit1.experiment())
    q1_list.append(q1)


    q2_list = []
    try:
        q2 = operators[1].operate(q1)
        qubit2 = Qubit(q2[0], q2[1])
        print(qubit2.experiment())
        q2_list.append(q2)
    except IndexError:
        pass
    q3_list = []
    try:
        q3 = operators[2].operate(q2)
        qubit3 = Qubit(q3[0], q3[1])
        print(qubit3.experiment())
        q3_list.append(q3)
    except IndexError:
        pass


    #print(qubit.experiment())
    print(" ")
