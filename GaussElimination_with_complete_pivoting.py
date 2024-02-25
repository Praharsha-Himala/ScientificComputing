import numpy as np


def GaussElimination_complete_pivoting(A_matrix, b_matrix):
    n = len(b_matrix)
    x = np.zeros(n)
    for k in range(0, n-1):
        max_row_index, max_col_index = np.unravel_index(np.argmax(A[k:, k:]), A[k:, k:].shape)
        print(max_row_index, max_col_index)
        A[[k, max_row_index + k]] = A[[max_row_index + k, k]]
        b[[k, max_row_index + k]] = b[[max_row_index + k, k]]
        A[:, [k, max_col_index + k]] = A[:, [max_col_index + k, k]]
    # print(A)
    # print(b)
    # print(max_row_index, max_col_index)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A_matrix[k, k] == 0:
                    if A_matrix[i, k] != 0:
                        A_matrix[[k, i]] = A_matrix[[i, k]]
                        b_matrix[[k, i]] = b_matrix[[i, k]]
            if A_matrix[i, k] == 0:
                pass
            else:
                factor = A_matrix[k, k] / A_matrix[i, k]
                for j in range(k, n):
                    A_matrix[i, j] = A_matrix[k, j] - A_matrix[i, j] * factor
                b_matrix[i] = b_matrix[k] - b_matrix[i] * factor

    x[n - 1] = b_matrix[n - 1] / A_matrix[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax = sum_ax + A_matrix[i, j] * x[j]
        x[i] = (b_matrix[i] - sum_ax) / A_matrix[i, i]
    return print(f"Procedure successful!\nSolution for the given A:\n{A_matrix}\n\nb: {b_matrix}\n\nx: {x}")


A = np.array([[0, 7, -1, 3, 1],
              [0, 3, 4, 1, 7],
              [6, 2, 0, 2, -1],
              [2, 1, 2, 0, 2],
              [3, 4, 1, -2, 1]], float)
b = np.array([5, 7, 2, 3, 4], float)

GaussElimination_complete_pivoting(A, b)
print(np.linalg.solve(A, b)) # for checking
