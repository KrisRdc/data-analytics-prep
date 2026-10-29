# 1. Create a dictionary with a menu and prices
menu = {"espresso": 1.50, "cappuccino": 2.20, "croissant": 2.00}

# 2. Access an existing item and a non-existing item safely using get()
price_espresso = menu.get("espresso", 0)
price_tea = menu.get("tea", 0)

# 3. Print the results to verify how get() handles missing keys
print("Espresso price:", price_espresso)
print("Tea price (missing):", price_tea)