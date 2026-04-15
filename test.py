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
    instance_list = []
    qubit_list = []


    for j in i:
        if j == '1.0':
            j = float(j)
            qubit_list.append(j)
        if j == '0.0':
            j = float(j)
            qubit_list.append(j)
        if j == 'X':
            op_list.append(j)
        if j == 'H':
            op_list.append(j)
        if j == 'f':
            op_list.append(j)
    print(qubit_list)
    #q = np.array([[i[0], i[1]]])
    #print(q)

    for sqo in op_list:
        if sqo == 'X':
            op_instance = SingleQubitOperator(sqo)
            instance_list.append(op_instance)
        if sqo == 'H':
            op_instance = SingleQubitOperator(sqo)
            instance_list.append(op_instance)
        else:
            pass


















