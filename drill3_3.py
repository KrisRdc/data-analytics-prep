#1. ask for occupied rooms and total rooms
occupied_rooms = int(input('Enter occupied rooms: '))
total_rooms = int(input('Enter total rooms: '))
# 2. calculate occupancy in percent, rounded to two decimals
percent =  round((occupied_rooms / total_rooms) * 100, 2)
# 3. print the occupancy and the level (low, medium, high)
print('Occupancy:', percent)   

if percent < 50:
    print('low')

elif percent <= 80:
    print('medium')    

else:
    print('high')   
