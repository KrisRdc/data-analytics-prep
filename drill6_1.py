# 1. Read the input dish name and remove leading and trailing whitespace using strip.
# 2. Check if the cleaned dish name is empty, and if so, print an error message and quit.
# 3. Print the dish name in uppercase letters along with its character count.

dish_name = input()
dish_name = dish_name.strip()

if dish_name == "":
    print("Error, dish name is empty")
    quit()

print("Dish:", dish_name.upper())
print("Length:", len(dish_name))