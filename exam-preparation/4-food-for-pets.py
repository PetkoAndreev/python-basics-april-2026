# Declaration of inputs
days_count = int(input())
total_food = float(input())

# Declaration of help variables
total_eaten_food = 0
total_dog_food = 0
total_cat_food = 0
total_biscuits = 0

# Loop for each day and read dog and cat food quantities
for day in range(1, days_count + 1):
    dog_food = int(input())
    cat_food = int(input())

    # Add the daily eaten food to the totals
    daily_eaten_food_total = dog_food + cat_food
    total_eaten_food += daily_eaten_food_total
    total_dog_food += dog_food
    total_cat_food += cat_food

    if day % 3 == 0:
        total_biscuits += daily_eaten_food_total * 0.10

# Calculate required percentages
eaten_food_percentage = total_eaten_food / total_food * 100
dog_food_percentage = total_dog_food / total_eaten_food * 100
cat_food_percentage = total_cat_food / total_eaten_food * 100

# Outputs
print(f'Total eaten biscuits: {round(total_biscuits)}gr.')
print(f'{eaten_food_percentage:.2f}% of the food has been eaten.')
print(f'{dog_food_percentage:.2f}% eaten from the dog.')
print(f'{cat_food_percentage:.2f}% eaten from the cat.')
