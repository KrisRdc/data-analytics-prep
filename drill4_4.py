def food_cost_percent(cost, revenue):
    return round(cost / revenue * 100, 2)

def food_cost_rating(percent):
    if percent <= 30:
        return 'good'
    elif percent <= 35:
        return 'borderline'
    else:
        return 'bad'

print(food_cost_percent(28, 100))
print(food_cost_rating(food_cost_percent(28, 100)))
print(food_cost_percent(30, 100))
print(food_cost_rating(food_cost_percent(30, 100)))
print(food_cost_percent(35, 100))
print(food_cost_rating(food_cost_percent(35, 100)))
print(food_cost_percent(40, 100))
print(food_cost_rating(food_cost_percent(40, 100)))