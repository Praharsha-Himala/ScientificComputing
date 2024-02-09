# Given list
my_list = [10, 1.5, -20, "Python", "100", "C", "Snake"]

# Task 1: Remove the element at index 5 and print the new list
del my_list[5]
print("1. List after removing element at index 5:", my_list)

# Task 2: Remove the element "C" and print the new list
my_list.remove("C")
print("2. List after removing element 'C':", my_list)

# Task 3: Add an element "C++" at the end of the list and print the new list
my_list.append("C++")
print("3. List after adding element 'C++' at the end:", my_list)

# Task 4: Remove all the ‘string’ elements from the list
my_list = [element for element in my_list if not isinstance(element, str)]
print("4. List after removing all 'string' elements:", my_list)

# Task 5: Find the largest number in the list from the previous step
largest_number = max(my_list)
print("5. Largest number in the list:", largest_number)
