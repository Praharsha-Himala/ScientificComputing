# Input: Get a sequence of comma-separated 4-digit binary numbers
binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Split the input into a list of binary numbers
numbers = binary_numbers.split(',')

# Use a list comprehension to filter numbers divisible by 5
result = [binary for binary in numbers if int(binary, 2) % 5 == 0]

# Output the result in a comma-separated sequence
print(','.join(result))
