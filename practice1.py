# 1. ask for food cost and food revenue
food_cost = float(input("Enter food cost: "))
food_revenue = float(input("Enter food revenue: "))
# 2. calculate food cost percentage
food_cost_percent = food_cost / food_revenue * 100
# 3. print the percentage and good / borderline / bad
print("Food cost:", food_cost_percent)
if food_cost_percent <= 30:
    print("good")
elif food_cost_percent <= 35:
    print("borderline")
else:
    print("bad")

