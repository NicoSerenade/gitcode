import numpy as np

a = np.array([1,2,3])
b = np.array([1,2,3])
print(a + b)
print(a * b)
print(a - b)
print(a / b)

data = np.array([1, 2, 3, 4, 5])
print(np.mean(data))  # Mean - promedio
print(np.sum(data))   # Sum - Sumatoria
print(np.std(data))   # Standard Deviation

a = np.array([1, 2, 3])
b = 2
print(a + b)  # Output: [3 4 5], adding 2 to each element of 'a'
print(a - b)

# Shape (3,3) (rows, columns)
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Extract a single element
print(data[0, 1])  # Output: 2 

# Extract a row
print(data[1, :])  # Output: [4, 5, 6]

# Extract a column
print(data[:, 1])  # Output: [2, 5, 8]

# Shape (2, 3, 4)(depth, rows, columns)

np3d = np.array([
    [[0,1,2,3], [4,5,6,7], [8,9,10,11]],
    [[12,13,14,15], [16,17,18,19], [20,21,22,23]]
])
print(np3d)
print(f'np3d.shape\n')
a1 = np3d[0,1,1] #access row 1, column 1 in layer 0
a2 = np3d[1,2,1] #access row 2, column 1 in layer 1
a3 = np3d[1,0, :] #extract row 0 layer 1
a4 = np3d[0, :, 1] #extract column 1 in layer 0
a5 = np3d[1] #extract layer 1
a6 = np3d[:, :, 0] #extract column 0
print(a6)

