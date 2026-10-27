# 1. Take user input and validate it is a number greater than 0
# 2. Decrement tables_waiting in each loop iteration and print status
# 3. Stop loop when tables reach 0 and print final message

try:
    tables_waiting = int(input())
except ValueError:
    print("Error, please enter numeric input")
    quit()

if tables_waiting <= 0:
    print("Error, enter a number greater than 0")
    quit()

while True:
    tables_waiting = tables_waiting - 1
    print("Tables waiting:", tables_waiting)
    if tables_waiting == 0:
        break

print("Service finished")