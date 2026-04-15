import numpy as np

n, p = 1, 0.36
s = np.random.binomial(n, p, 100)
print(np.bincount(s))

q = np.random.binomial(1, 1, 100)
v = np.bincount(q)
print(v[0])
print(v[1])

j = np.random.binomial(0, 1, 100)
print(np.bincount(j))


#unique, frequency = np.unique(s, return_counts = True)
#print("unique values", unique)
#print("Frequency: ", frequency)
#print(unique[0], frequency[0])
#print(unique[1], frequency[1])

#print (f'Percentage of 0 measured: {frequency[0]}' + "\n" + f'Percentage of 1 measured: {frequency[1]}' )
