import numpy.linalg as alg
import numpy as np

A = np.array([[10, -1, 2, 0.],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0., 3, -1, 8]])

b = np.array([6, 25, -11, 15])

n = len(A)


# print(x0)

def jacobi_iterative(A_matrix, b_matrix, max_iter: int = 100, tol: float = 0.0001):

    x0 = np.zeros(len(A_matrix))
    x = np.zeros(len(A_matrix))
    for iteration in range(max_iter):
        for i in range(len(A_matrix)):
            dum_sum = 0
            for j in range(len(A_matrix)):
                if j != i:
                    dum_sum += A_matrix[i][j] * x0[j]
            x[i] = (- dum_sum + b_matrix[i]) / A_matrix[i][i]
        if abs(alg.norm(x - x0)) < tol:
            print(f"The solution at {iteration} iteration\nx: {x}")
            raise Warning('The procedure is successful')

    return print(f"Maximum iterations reached!\n The solution at {iteration} iteration\nx: {x}")


jacobi_iterative(A, b, max_iter=1000)
