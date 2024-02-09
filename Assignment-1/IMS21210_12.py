# Input: Get the number of elements in the array from the user
num_elements = int(input("Input the number of elements to be stored in the array: "))

# Input: Get the elements of the array from the user
array = []
for i in range(num_elements):
    array.append(int(input(f"element - {i} : ")))

# Count the frequency of each element
frequency = {}
for element in array:
    frequency[element] = frequency.get(element, 0) + 1

# Output the frequency of each element
print("The frequency of all elements of an array:")
for element, count in frequency.items():
    print(f"{element} occurs {count} times")
