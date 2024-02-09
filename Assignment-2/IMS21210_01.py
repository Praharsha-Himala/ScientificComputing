# Gaussian Elimination with Partial Pivoting
"""
Gaussian Elimination with Partial Pivoting is a numerical method for solving systems of linear equations. It is an
extension of the Gaussian Elimination method, which aims to transform a given system of linear equations into an
upper triangular form through a series of elementary row operations.

Partial pivoting is introduced to avoid division by zero and to enhance numerical stability. In partial pivoting,
at each step, the algorithm selects the pivot element as the one with the maximum absolute value from the current
column."""
def gauss_elimination_partial_pivot(A, b):
    n = len(b)

    # Augmenting the matrix
    for i in range(n):
        A[i].append(b[i])

    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = max(range(i, n), key=lambda k: abs(A[k][i]))
        A[i], A[max_row] = A[max_row], A[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n + 1):
                A[j][k] -= factor * A[i][k]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for j in range(i - 1, -1, -1):
            A[j][n] -= A[j][i] * x[i]

    return x

# Test system of linear equations
A = [
    [2, -1, 1],
    [-3, 2, 2],
    [1, 1, 1]
]
b = [8, -3, 6]

# Solve the system using Gaussian Elimination with Partial Pivoting
solution = gauss_elimination_partial_pivot(A, b)

# Output the test system and the solution
print("Test System of Linear Equations:")
for i in range(len(A)):
    equation = ' + '.join([f"{A[i][j]}x{j+1}" for j in range(len(A[i]))])
    print(f"{equation} = {b[i]}")

print("\nSolution obtained by Gaussian Elimination with Partial Pivoting:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
