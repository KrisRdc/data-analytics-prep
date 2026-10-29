# 1. Create an unsorted list of inventory items
inventory = [50, 10, 30, 20, 40]
print("Unsorted inventory:", inventory)

# 2. Sort the list in place using sort()
inventory.sort()
print("Sorted inventory:", inventory)

# 3. Loop through the sorted list and print each item
for item in inventory:
    print("Inventory level:", item)