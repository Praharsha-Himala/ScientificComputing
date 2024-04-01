import numpy as np

A = np.array([[-2, -3], [6, 7]])
x0 = np.array([1, 1])

def power_method(input_matrix, vector, max_iterations = 100, TOL= 0.0001):
    x0 = vector.T
    mu = 0
    for i in range(6):
        x_new = np.dot(A, x0)
        mu_new = max(x_new) / max(x0)

        if abs(mu_new - mu) < TOL:
            break
        else:
            x0 = x_new
            mu = mu_new
    eigen = x_new/ np.max(x_new)
    return eigen, mu

print(power_method(A, x0))