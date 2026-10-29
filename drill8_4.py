# 1. Create a sentence or a line of text with space-separated values (e.g., numbers or items)
sentence = "coffee tea juice water"
print("Original:", sentence)

# 2. Use the split() method to break the string into a list of words/items
words = sentence.split()

# 3. Print the resulting list and count how many items it contains using len()
print("List of woed:", words)
word_count = len(words)
print("Total words:", word_count)
