# Input: Get a comma-separated sequence of words
input_words = input("Enter a comma-separated sequence of words: ")

# Split the input into a list of words
words = input_words.split(',')

# Sort the words alphabetically
sorted_words = sorted(words)

# Output the result in a comma-separated sequence
print(','.join(sorted_words))
