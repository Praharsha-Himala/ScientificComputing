# Input: Get a decimal number from the user
decimal_number = int(input("Enter a number to convert: "))

# Initialize an empty string to store the binary representation
binary_representation = ""

# Convert decimal to binary
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number //= 2

# Output the result
print(f"The Binary of {decimal_number} is {binary_representation}.")
