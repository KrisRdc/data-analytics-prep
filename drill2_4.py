weekly_wages = float(input('Enter weekly wages: '))
weekly_revenue = float(input('Enter weekly revenue: '))

labour_cost = (weekly_wages / weekly_revenue) * 100

print('Labour cost:', labour_cost)