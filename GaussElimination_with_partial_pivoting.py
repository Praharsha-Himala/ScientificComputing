import numpy as np


# defining gauss elimination with partial pivoting function
def GaussElimination_partial_pivoting(A_matrix, b_matrix):
    # creating a copy of A_matrix, b_matrix
    A = A_matrix.copy()
    b = b_matrix.copy()
    n = len(b_matrix)  # size of the matrix
    x = np.zeros(n)  # solution variable for system of linear variables
    for k in range(0, n - 1):  # initialization of k loop with values 0, ..., n-2
        if np.fabs(A_matrix[k, k]) < 1.0e-10:  # if pivot elements of the rows are very, very small
            max_index = k  # defining maximum element as the first element if it's less than 1.0e-12
            for i in range(k + 1, n):  # initialization of i loop for checking which first element in the matrix is
                # larger so that we can swap it with the row having zero or less as first element
                if A_matrix[i, k] > A_matrix[max_index, k]: # searching for maximum value
                    max_index = i  # storing the maximum value row index
            A_matrix[[k, max_index]] = A_matrix[[max_index, k]]  # interchanging rows in A matrix
            b_matrix[[k, max_index]] = b_matrix[[max_index, k]]  # interchanging b values
        # usual gauss elimination i loop initialization with value k+1, ..., n-1
        for i in range(k + 1, n):
            if A_matrix[i, k] == 0:  # if first element is zero then its property of lower triangular matrix
                pass  # then we move to next row
            else:
                factor = A_matrix[k, k] / A_matrix[i, k]  # calculation scaling factor
                for j in range(k, n):  # j loop with values k,...,n-1
                    A_matrix[i, j] = A_matrix[k, j] - A_matrix[i, j] * factor  # elimination

                b_matrix[i] = b_matrix[k] - b_matrix[i] * factor  # changing b_matrix with elimination
    # 2. Back Substitution
    x[n - 1] = b_matrix[n - 1] / A_matrix[n - 1, n - 1]  # getting the value of the last row of A_matrix
    for i in range(n - 2, -1, -1):  # i loop from n-2, ..., 0  from backwards; here we put -1 as the last element
        # as the range function takes one element before last row index
        sum_ax = 0  # summation initialization
        for j in range(i + 1, n):  # j loop from i+1 to n-1
            sum_ax = sum_ax + A_matrix[i, j] * x[j]  # summation term
        x[i] = (b_matrix[i] - sum_ax) / A_matrix[i, i]  # solution for each equation

    return print(f"Procedure successful!\nSolution for the given A:\n{A}\n\nb: {b}\n\nx: {x}")


#########################################################################################################
A = np.array([[0, 7, -1, 3, 1],
              [0, 3, 4, 1, 7],
              [6, 2, 0, 2, -1],
              [2, 1, 2, 0, 2],
              [3, 4, 1, -2, 1]], float)
b = np.array([5, 7, 2, 3, 4], float)

GaussElimination_partial_pivoting(A, b)
# print(np.linalg.solve(A, b))