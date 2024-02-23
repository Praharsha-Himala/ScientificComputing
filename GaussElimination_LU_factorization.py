import numpy as np
from scipy.linalg import solve, lu

A = np.array([ [1, 1, 0, 3],
               [2, 1, -1, 1],
               [3, -1, -1, 2],
               [-1, 2, 3, -1]
])
b = np.array([4, 1, -3, 4])
U = np.copy(A)
b_c = np.copy(b)
print(A.shape)
L = np.zeros(A.shape)
for i in range(len(L)):
    for j in range(len(L)):
        if i == j:
            L[i, j] = 1
print(L)

n = len(A)
for k in range(0, n - 1):
    for i in range(k+1, n):
        factor = A[i, k] / A[k, k]
        for j in range(k, n):
            A[i, j] = A[i, j] - A[k, j] * factor
        b[i] = b[i] - b[k] * factor
        L[i, k] = factor
print(A)
print(b)
print(L)

x = np.zeros(n)
y = np.zeros(n)



print("Solution x:", x)
