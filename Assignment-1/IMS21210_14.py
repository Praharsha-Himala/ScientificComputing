def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Input: Get a number from the user
num = int(input("Enter a number to compute its factorial: "))

# Calculate the factorial using the factorial function
result = factorial(num)

# Output the result
print(f"The factorial of {num} is: {result}")
