# Declaration of inputs
strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

# Calculate other fruits prices
raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (0.4 * raspberry_price)  # Alternative 0.6 * raspberry_price
banana_price = 0.2 * raspberry_price  # Alternative raspberry_price - (0.8 * raspberry_price)

# Calculate total amount of all fruits
total_strwaberry_price = strawberry_price * strawberry_quantity
total_banana_price = banana_price * banana_quantity
total_raspberry_price = raspberry_price * raspberry_quantity
total_orange_price = orange_price * orange_quantity

total_price = total_strwaberry_price + total_banana_price + total_raspberry_price + total_orange_price

print(f'{total_price:.2f}')
