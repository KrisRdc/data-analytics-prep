# 1. Create a list of sample prices or revenues
income = [120.5, 45.0, 300.25, 89.9]
print("Income", income)
# 2. Sort the list, append a new value, and check its length using len()
income.append(123)
income.sort()
total_items = len(income)

# 3. Print the sorted list, the new item added, and the final length
print("Sortet Income:", income)
print("Final lenght:", total_items)
