# Input: Get the size of the array from the user
size = int(input("Input the size of the array: "))

# Input: Get the elements of the array from the user
array = []
for i in range(size):
    array.append(int(input(f"element - {i} : ")))

# Sort the array in ascending order
array.sort()

# Output the sorted elements
print("Elements of array in sorted ascending order:")
print(' '.join(map(str, array)))
