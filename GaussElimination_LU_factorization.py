import numpy as np

A = np.array([ [1, 1, 0, 3],
               [2, 1, -1, 1],
               [3, -1, -1, 2],
               [-1, 2, 3, -1]
])
print(A.shape)
L = np.zeros(A.shape)
for i in range(len(L)):
    for j in range(len(L)):
        if i == j:
            L[i, j] = 1
print(L)
b = np.array([4, 1, -3, 4])
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
y = np.zeros(n)
y[n - 1] = b[n - 1] / A[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    sum_ax = 0
    for j in range(i+1, n):
        sum_ax = sum_ax + A[i, j] * y[j]
    y[i] = (b[i] - sum_ax) / A[i, i]


x = np.zeros(n)
x[0] = y[0]
for i in range(1, n):
    sum_x = 0
    for j in range(0, n - 1):
        sum_x = sum_x + L[j, j-1] * x[j - 1]
    x[i] = (y[i] - sum_x) / L[i, i]

print(x)


def GaussElimination_LU(A_matrix, b_matrix):
    return

import numpy as np
from scipy.linalg import lu, solve

# Given matrix A and vector b
A = np.array([
    [1, 1, 0, 3],
    [2, 1, -1, 1],
    [3, -1, -1, 2],
    [-1, 2, 3, -1]
])

b = np.array([4, 1, -3, 4])

# Perform LU decomposition
P, L, U = lu(A)

# Solve Ly = b for y
y = solve(L, b)

# Solve Ux = y for x
x = solve(U, y)

print("Solution x:", x)
