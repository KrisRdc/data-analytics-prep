# 1. ask for weekly wages and weekly revenue, stop if either is not a number
# 2. stop if the revenue is not greater than 0
# 3. calculate the labour cost with a function and print it

def labour_cost_percent(wages, revenue):
    return round(wages / revenue * 100, 2)

try:
    weekly_wages = float(input('Enter weekly wages: '))
    weekly_revenue = float(input('Enter weekly revenue: '))
except:
    print('Error, please enter numeric input')
    quit()

if weekly_revenue <= 0:
    print('Error, revenue must be greater than 0')
    quit()

print('Labour cost:', labour_cost_percent(weekly_wages, weekly_revenue))