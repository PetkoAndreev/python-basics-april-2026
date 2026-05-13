# Declaration of inputs
trip_price = float(input())

# Toys counts
puzzle_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
toy_trucks_count = int(input())

# Set toys prices
puzzle_price = 2.60
talking_doll_price = 3.00  # To ensure it is float
teddy_bear_price = 4.10
minion_price = 8.20
toy_truck_price = 2.00  # To ensure it is float

# Get total count of ordered toys
total_toys_count = (
        puzzle_count + \
        talking_dolls_count + \
        teddy_bears_count + \
        minions_count + \
        toy_trucks_count
)

# Get total price of the ordered toys
total_order_price = (puzzle_count * puzzle_price) \
                    + (talking_dolls_count * talking_doll_price) \
                    + (teddy_bears_count * teddy_bear_price) \
                    + (minions_count * minion_price) \
                    + (toy_trucks_count * toy_truck_price)
# Check if ordered toys are at least 50 or great thatn 50
if total_toys_count >= 50:
    total_order_price -= total_order_price * 0.25  # Equivalent to total_order_price = total_order_price - (total_order_price * 0.25) Option 2 - 100 - 25 = 75% => total_order_price = total_order_price * 0.75
# Calculate 10% rent for the store
rent = total_order_price * 0.10
# Calculate the profit for the holiday
profit = total_order_price - rent

# Check if the profit is enough to go to Holiday
if profit >= trip_price:
    money_left = profit - trip_price # Alternative - round(profit - trip_price, 2)
    print(f'Yes! {money_left:.2f} lv left.')
else:
    needed_money = trip_price - profit  # Alternative is abs(profit - trip_price)
    print(f'Not enough money! {needed_money:.2f} lv needed.')
