import numpy as np
A = np.array([[1, 1, 0, 3],
              [2, 1, -1, 1],
              [3, -1, -1, 2],
              [-1, 2, 3, -1]
              ])
b = np.array([8, 7, 14, -7])
U = np.copy(A)

L = np.zeros(A.shape)
for i in range(len(L)):
    for j in range(len(L)):
        if i == j:
            L[i, j] = 1
# print(L)

n = len(A)
for k in range(0, n - 1):
    for i in range(k + 1, n):
        factor = A[i, k] / A[k, k]
        for j in range(k, n):
            A[i, j] = A[i, j] - A[k, j] * factor
        b[i] = b[i] - b[k] * factor
        L[i, k] = factor
print(A)
# print(b)
# print(L)

x = np.zeros(n)
y = np.zeros(n)
y[0] = b[0] / L[0, 0]
for i in range(1, n):
    sum_ax = 0
    for j in range(0, i - 1):
        sum_ax = sum_ax + (L[i, j] * y[j])
    y[i] = (b[i] - sum_ax) / L[i, i]
print(L)
print(y)

x[n - 1] = b[n - 1] / A[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    sum_xx = 0
    for j in range(i+1, n):
        sum_xx += A[i, j] * x[j]
    x[i] = (y[i] - sum_xx ) / A[i, i]

print(x)