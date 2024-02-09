# Input: Get the number for which the multiplication table needs to be calculated
number = int(input("Input the number (Table to be calculated): "))

# Display the multiplication table up to 10
print(f"Multiplication Table of {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} X {i} = {result}")
