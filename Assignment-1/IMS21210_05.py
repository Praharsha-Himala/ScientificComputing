# Input: Get the amount from the user
amount = int(input("Input the amount: "))

# Define the denominations of banknotes
denominations = [100, 50, 20, 10, 5, 2, 1]

# Initialize a dictionary to store the count of each denomination
note_count = {}

# Calculate the number of each denomination
for denomination in denominations:
    count = amount // denomination
    note_count[denomination] = count
    amount %= denomination

# Output the result
print("There are:")
for denomination, count in note_count.items():
    print(f"{count} Note(s) of {denomination:.2f}")
