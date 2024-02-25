import numpy as np


# Defining gauss elimination function
def Gauss_elimination(A_matrix, b_matrix):
    n = len(b_matrix)  # taking n as size of b_matrix; for example say n = 4
    x = np.zeros(n, float)  # creating a solution matrix which will be updated
    # 1. Elimination
    for k in range(0, n - 1):  # k loop from 0, ..., n-2 for fixed rows and columns; the k values will be 0, 1, 2.
        for i in range(k + 1, n):  # i loop from k+1, ..., n-1 to process elimination for rows except the first row;
            # i values will be 1, 2, 3.
            if A_matrix[k, k] == 0:
                if A_matrix[i, k] != 0:
                    A_matrix[[k, i]] = A_matrix[[i, k]]  # swapping rows with non zero row element
                    b_matrix[[k, i]] = b_matrix[[i, k]]
            if A_matrix[i, k] == 0:  # checking if the first element of the row is zero
                pass  # then move to next row
            factor = A_matrix[i, k] / A_matrix[k, k]  # calculating scaling factor
            for j in range(k, n):  # j loop from k, ..., n-1 to eliminate/make an upper triangular matrix; j values
                # will be 0, 1, 2.
                A_matrix[i, j] = A_matrix[i, j] - A_matrix[k, j] * factor  # Elimination
            b_matrix[i] = b_matrix[i] - b_matrix[k] * factor  # changing b_matrix along with elimination

    # 2. Back substitution
    x[n - 1] = b_matrix[n - 1] / A_matrix[n - 1, n - 1]  # getting the value of the last row of A_matrix
    for i in range(n - 2, -1, -1):  # i loop from n-2, ..., 0  from backwards; here we put -1 as the last element
        # as the range function takes one element before last row index
        sum_ax = 0  # summation initialization
        for j in range(i + 1, n):  # j loop from i+1 to n-1
            sum_ax += A_matrix[i, j] * x[j]  # summation term
        x[i] = (b_matrix[i] - sum_ax) / A_matrix[i, i]  # solution for each equation

    return print(f"Procedure successful!\nSolution for the given A:\n{A_matrix}\n\nb: {b_matrix}\n\nx: {x}")
    # printing solution of the equation


#########################################################################################################
A = np.array([[3, -2, 5, 0],
              [4, 5, 8, 1],
              [1, 1, 2, 1],
              [2, 7, 6, 5]], float)
b = np.array([2, 4, 5, 7], float)

Gauss_elimination(A, b)
