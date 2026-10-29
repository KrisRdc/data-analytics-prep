# 1. Read orders.txt and count drink frequencies into a dictionary
fname = "orders.txt"
try:
    handle = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

counts = dict()
for line in handle:
    drink = line.rstrip()
    counts[drink] = counts.get(drink, 0) + 1

# 2. Loop through the dictionary to find the drink with the maximum order count
bigname = None
bigcount = None
for drink, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigname = drink

# 3. Print the most frequent drink and its total count
print("Most frequent drink:", bigname, "with", bigcount, "orders")