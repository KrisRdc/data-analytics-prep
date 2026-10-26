def occupancy_level(percent):
    if percent < 50:
        return 'low'
    elif percent <= 80:
        return 'medium'
    else:
        return 'high'

occupied_rooms = int(input('Enter occupied rooms: ')) 
total_rooms = int(input('Enter total rooms: '))  
percent = round(occupied_rooms / total_rooms * 100, 2)
       
print('Occupancy:', percent)
print(occupancy_level(percent))