with open("qubits.txt", 'rb') as f:
    contents = f.read()
contents = contents.decode("utf-16").rstrip().split("\n")
print(contents)
print(contents[0])
print(contents[0][0])

for i in contents:
    i = i.split(" ")
    i[0] = float(i[0])
    i[1] = float(i[1])
    print(i)
    print("The initial state of the Qubit is: " + str(i[0]) + "|0>" + " " "+" + " " + str(i[1]) + "|1>")

