import numpy as np
import math
from qubit import Qubit
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


    for j in i:
        if j != 'X' and j !='H' and j !='f':
            j = float(j)
            qubit_list.append(j)
        #if j == 'X' or j =='H' :
            #op_list.append(j)
        else:
            pass

        #for oper in op_list:
            #op_instance = SingleQubitOperator(oper)
            #instance_list.append(op_instance)


    q = np.array([[qubit_list[0]], [qubit_list[1]]])
    q_ins = Qubit(qubit_list[0], qubit_list[1])

























