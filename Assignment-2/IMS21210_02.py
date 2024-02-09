"""Gaussian Elimination with Complete Pivoting is another numerical method for solving systems of linear equations.
In this method, at each step, the algorithm selects the pivot element as the one with the maximum absolute value from
the entire matrix, including both rows and columns.
"""
# Gaussian Elimination with Complete Pivoting

def gauss_elimination_complete_pivot(A, b):
    n = len(b)

    # Augmenting the matrix
    for i in range(n):
        A[i].append(b[i])

    # Forward elimination
    for i in range(n):
        # Complete pivoting
        max_val = 0
        pivot_row = -1
        pivot_col = -1

        for row in range(i, n):
            for col in range(i, n + 1):
                if abs(A[row][col]) > max_val:
                    max_val = abs(A[row][col])
                    pivot_row = row
                    pivot_col = col

        A[i], A[pivot_row] = A[pivot_row], A[i]
        for row in range(n):
            A[row][i], A[row][pivot_col] = A[row][pivot_col], A[row][i]

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

# Solve the system using Gaussian Elimination with Complete Pivoting
solution = gauss_elimination_complete_pivot(A, b)

# Output the test system and the solution
print("Test System of Linear Equations:")
for i in range(len(A)):
    equation = ' + '.join([f"{A[i][j]}x{j+1}" for j in range(len(A[i]))])
    print(f"{equation} = {b[i]}")

print("\nSolution obtained by Gaussian Elimination with Complete Pivoting:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
