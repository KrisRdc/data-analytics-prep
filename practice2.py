# 1. ask for the bill amount
bill = float(input("Enter bill amount: "))
# 2. work out the tip percentage from the bill amount
if bill <= 20:
    tip_percent = 0.05
elif bill <= 50:
    tip_percent = 0.10
else:
    tip_percent = 0.10

# 3. print the tip and the total

tip = bill * tip_percent
total = bill + tip 


print("Tip: ", + str(tip) + "| Total: " + str(total))