# 1. create a list of items and start the total at zero
# 2. loop over the list and add each item to the total
# 3. after the loop, add the service charge and print the rounded total

items = [18, 42, 25, 15]
total = 0
for item in items:
    total = total + item
total = total * 1.10
print('Total with service:',round(total,2))