bill = float(input('Enter bill amount: '))

if bill < 20:
    tip = bill * 0.05

elif bill <= 50:
    tip = bill * 0.10

else:
    tip = bill * 0.15
    
tip = round(tip, 2)
total = bill + tip

print('Tip:', tip)
print('Total:', total)