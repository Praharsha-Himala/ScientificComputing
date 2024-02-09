# Given dictionary
mark = {'A': 60, 'B': 50, 'C': 80, 'D': 70, 'E': 40}

# Task 1: Add a key-value pair 'F': 30 and print the resulting dict
mark['F'] = 30
print("1. Dictionary after adding 'F': 30:", mark)

# Task 2: Check whether the key 'X' exists in the dict and print the result
key_to_check = 'X'
print(f"2. Does key '{key_to_check}' exist? {'Yes' if key_to_check in mark else 'No'}")

# Task 3: Print the list of all the keys in the dict
print("3. List of all keys:", list(mark.keys()))

# Task 4: Print the list of all the values in the dict
print("4. List of all values:", list(mark.values()))

# Task 5: Sort the dict by value and print the new dict
sorted_mark = dict(sorted(mark.items(), key=lambda x: x[1]))
print("5. Sorted dict by value:", sorted_mark)
