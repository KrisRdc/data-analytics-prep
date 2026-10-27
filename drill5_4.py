# Initialize variables to find the best, worst, and calculate the difference
# Loop through the list of revenue values to update maximum and minimum
# Print the best day, worst day, and the difference between them

revenues = [1250, 980, 1430, 870, 1100]
best_day = None
worst_day = None

for amount in revenues:
    if best_day is None or amount > best_day:
        best_day = amount
    if worst_day is None or amount < worst_day:
        worst_day = amount

difference = best_day - worst_day

print("Best day:", best_day)
print("Worst day:", worst_day)
print("Difference:", difference)