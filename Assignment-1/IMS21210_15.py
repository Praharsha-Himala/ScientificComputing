# Input: Get a sequence of comma-separated numbers
input_numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input into a list of numbers
numbers_list = input_numbers.split(',')

# Convert the list of numbers to a tuple
numbers_tuple = tuple(numbers_list)

# Output the list and tuple
print("List:", numbers_list)
print("Tuple:", numbers_tuple)
