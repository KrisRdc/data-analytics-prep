# Read and clean the input string for formatting
# Find the semicolon position and handle missing separators
# Slice the string to extract and print the dish name and price

dish_line = input()
dish_line = dish_line.strip()

semicolon = dish_line.find(";")

if semicolon == -1:
  print("Error, no semicolon found")
  quit()

name = dish_line[:semicolon]
price = dish_line[semicolon + 1 :]

print("Name:", name)
print("Price:", price)