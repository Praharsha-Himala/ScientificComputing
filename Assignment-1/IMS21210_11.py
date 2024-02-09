# Use a list comprehension to find numbers meeting the criteria
result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]

# Output the result in a comma-separated sequence on a single line
print(','.join(result))
