def harmonic_series(n):
    if n == 1:
        return "1/1", 1.0
    else:
        prev_series, prev_sum = harmonic_series(n - 1)
        term = 1 / n
        current_series = f"{prev_series} + 1/{n}"
        current_sum = prev_sum + term
        return current_series, current_sum

# Input: Get the number of terms from the user
n = int(input("Input the number of terms: "))

# Calculate the harmonic series and its sum using recursion
series, sum_of_series = harmonic_series(n)

# Output the result
print(f"The Harmonic Series: {series}")
print(f"Sum of Series upto {n} terms: {sum_of_series}")
