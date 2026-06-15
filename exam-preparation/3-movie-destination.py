# Declaration of inputs
budget = float(input())
destination = input()
season = input()
days_count = int(input())

# Determine the price per shooting day by destination and season
price_per_day = 0

if destination == 'Dubai':
    if season == 'Winter':
        price_per_day = 45000 * 0.70 # Apply 30% discount for destination Dubai
    elif season == 'Summer':
        price_per_day = 40000 * 0.70 # Apply 30% discount for destination Dubai
elif destination == 'Sofia':
    if season == 'Winter':
        price_per_day = 17000 * 1.25 # Apply 25% tax for destination Sofia
    elif season == 'Summer':
        price_per_day = 12500 * 1.25 # Apply 25% tax for destination Sofia
elif destination == 'London':
    if season == 'Winter':
        price_per_day = 24000
    elif season == 'Summer':
        price_per_day = 20250

# Calculate the total movie cost before taxes
total_cost = days_count * price_per_day

# Apply destination discount/tax
# if destination == 'Dubai':
#     total_cost *= 0.70 # Alternative total_cost - (0.30 * total_cost)
# elif destination == 'Sofia':
#     total_cost *= 1.25 # Alternative total_cost + (0.25 * total_cost)

# Outputs
if budget >= total_cost:
    print(f'The budget for the movie is enough! We have {budget - total_cost:.2f} leva left!')
else:
    print(f'The director needs {total_cost - budget:.2f} leva more!')
