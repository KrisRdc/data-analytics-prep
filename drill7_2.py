# 1. Prepare file handle, total revenue accumulator, and day count
handle = open("revenue.txt")
revenue_total = 0
revenue_count = 0
# 2. Loop through each line, find semicolon, extract revenue value as float, and update totals
for line in handle:
    line = line.strip()
    semicolon = line.find(";")
    amount = float(line[semicolon + 1:])
    revenue_total = revenue_total + amount
    revenue_count = revenue_count + 1

# 3. Calculate average revenue and print total and average results
# 3. Calculate average revenue and print total and average results
if revenue_count > 0:
    average_revenue = revenue_total / revenue_count
    print("Total revenue:", revenue_total)
    print("Average revenue:", average_revenue)
else:
    print("No revenue data found.")