# Input: Get a binary number from the user
binary_number = input("Input a binary number: ")

# Initialize the decimal result to 0
decimal_number = 0

# Convert binary to decimal
for digit in binary_number:
    decimal_number = decimal_number * 2 + int(digit)

# Output the result
print("The Binary Number:", binary_number)
print("The equivalent Decimal Number:", decimal_number)
