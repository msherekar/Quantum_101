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
    op_list = []
    instance_list = []
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

    operators.insert(0, q)
    results = []

    for n in operators[1:]:
        results.append(n.operate(operators[0]))


    qubit = Qubit(q[0], q[1])
    print(qubit.__str__())
    print(results[0])
    print(qubit.experiment())
    print(" ")












