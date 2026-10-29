# 1. Ask the user for a file name and open it with error handling
fname = "orders.txt"
try:
    handle = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

# 2. Read the file line by line, clean the text, and count each drink using a dictionary and get()
counts = dict()
for line in handle:
    drink = line.rstrip()
    counts[drink] = counts.get(drink, 0) + 1

# 3. Print the final counts dictionary
print("Drink counts:", counts)