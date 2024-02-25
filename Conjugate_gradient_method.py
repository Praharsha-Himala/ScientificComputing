import numpy as np
A = np.array([[3, -2, 5, 0],
              [4, 5, 8, 1],
              [1, 1, 2, 1],
              [2, 7, 6, 5]], float)
b = np.array([2, 4, 5, 7], float)

x = np.zeros(len(b))

r = b - np.dot(A, x)
p = r
for iteration in range(1000):
    Apk = np.dot(A, p)
    alpha = np.dot(r.T, r) / np.dot(p.T, Apk)
    x_k = x
    r_k = r
    x = x + np.dot(alpha, p)
    r = r - np.dot(alpha, Apk)
    beta = np.dot(r.T, r) / np.dot(r_k.T, r_k)
    p = r + np.dot(beta, p)