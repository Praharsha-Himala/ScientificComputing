# Given string
my_string = "Python is a programming language, that lets you work quickly"

# Task 1: Print the last character
last_character = my_string[-1]
print("1. Last character:", last_character)

# Task 2: Write a statement that prints the , (comma) character
comma_character = ','
print(f"2. {comma_character} character:", comma_character)

# Task 3: Print the index of the 'w' character
index_of_w = my_string.index('w')
print("3. Index of 'w' character:", index_of_w)

# Task 4: Find and print the number of occurrences of the character 'a'
occurrences_of_a = my_string.count('a')
print("4. Number of occurrences of 'a':", occurrences_of_a)

# Task 5: Convert all the letters into upper case and print the string
uppercase_string = my_string.upper()
print("5. Uppercase string:", uppercase_string)

# Task 6: Split string into two parts using the , (comma) as the delimiter and print the two parts
two_parts = my_string.split(',')
print("6. Two parts after splitting with comma as delimiter:", two_parts)
