import numpy as np

def GaussElimination_complete_pivoting(A_matrix, b_matrix):
    n = len(b_matrix)
    x = np.zeros(n)
    for k in range(0, n-2):
        print(A_matrix[k, 0])
        if 1.0e-10 > abs(A_matrix[k, 0]):
            max_row_index, max_col_index = np.unravel_index(A_matrix[k+1:,].argmax(), A_matrix.shape)
            print(max_row_index, max_col_index)
            A_matrix[[k, max_row_index+1]] = A_matrix[[max_row_index+1, k]]
            b_matrix[[k, max_row_index+1]] = b_matrix[[max_row_index+1, k]]
            print(A_matrix)
            A_matrix[:,[k, max_col_index]] = A_matrix[:, [max_col_index, k]]
            print(A_matrix)

# Your provided matrix
A = np.array([[0, 7, -1, 3, 1],
                    [0, 3, 4, 1, 7],
                    [6, 2, 0, 2, -1],
                    [2, 1, 2, 0, 2],
                    [3, 4, 1, -2, 1]], float)
b = np.array([5, 7, 2, 3, 4], float)

GaussElimination_complete_pivoting(A, b)

# i, j = np.unravel_index(a[1:,].argmax(), a.shape)
# max_row_index = i+1
# max_col_index = j
#
#
# a[[0, max_row_index]] = a[[max_row_index, 0]]
#
# print(a)
#
# a[:, [0, max_col_index]] = a[:, [max_col_index, 0]]


