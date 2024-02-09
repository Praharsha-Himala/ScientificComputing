# Input: Get a sequence of comma-separated numbers
input_numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input into a list of integers
numbers = [int(num) for num in input_numbers.split(',')]

# Use a list comprehension to square each odd number
result = [num**2 for num in numbers if num % 2 != 0]

# Output the result
print(','.join(map(str, result)))
