# Iterates through daily guest numbers to update the total count and cumulative sum
# Calculates the average number of guests per day if valid data is present
# Prints the calculated average rounded to two decimal places or handles missing data
daily_guests = [82, 95, 70, 110]
day_count = 0
guests_sum = 0
for guests_in_day in daily_guests:
    day_count = day_count + 1
    guests_sum = guests_sum + guests_in_day

if day_count > 0:
    average_guests = guests_sum / day_count
    print('Average guests:', round(average_guests, 2))
else:
    print('No guest data')