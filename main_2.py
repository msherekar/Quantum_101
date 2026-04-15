import numpy as np
import math
from qubit import Qubit
from operator2 import SingleQubitOperator

# Read the file contents (Done)
with open("qubits.txt", 'rb') as f:
    contents = f.read()
contents = contents.decode("utf-16").rstrip().split("\n")


for i in contents:

    i = i.split(" ")
    op_list = []

    for j in i:
        if j == '1.0' or '0.0':
            j = float(j)

        else:
            op_instance = SingleQubitOperator(j)
            op_list.append(op_instance)
    q = np.array([i[0], i[1]])

    for i in op_list:
        np.matmul(q, i)
        # multiply q by each sequentially and print out final result
        # store final qubit to apply experiment

    # creating instance of qubit class by passing alpha and beta from each line
    q = Qubit(i[0], i[1])

# extract alpha and beta create an qubit i.e numpy array