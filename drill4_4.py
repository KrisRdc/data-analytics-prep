def food_cost_percent(cost, revenue):
    return round(cost / revenue * 100, 2)

def food_cost_rating(percent):
    if percent <= 30:
        return 'good'
    elif percent <= 35:
        return 'borderline'
    else:
        return 'bad'

try:
    food_cost = float(input('Enter food cost: '))
    food_revenue = float(input('Enter food revenue: '))


except:
    print('Error, please enter numeric input')
    quit()

if food_revenue <= 0:
    print('Error, revenue must be greater than 0')
    quit()

percent = food_cost_percent(food_cost, food_revenue)
print('Food cost:', percent)
print(food_cost_rating(percent))
