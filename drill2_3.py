guests = int(input('Enter number of guests: '))
seats_per_table = 4

full_tables = guests // seats_per_table
guests_left_over = guests % seats_per_table

print('Full tables:',full_tables)
print('Guests left over:', guests_left_over)