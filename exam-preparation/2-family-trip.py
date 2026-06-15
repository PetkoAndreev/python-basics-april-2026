# Declaration of inputs
budget = float(input())
nights_counts = int(input())
price_per_night = float(input())
extra_expenses_percentage = int(input())

# Apply 5% discount if nights are more than 7
if nights_counts > 7:
    price_per_night *= 0.95 # Alternative price_per_night - (0.05 * price_per_night)

# Calculate expenses
accommodation_cost = nights_counts * price_per_night
extra_expenses = budget * extra_expenses_percentage / 100
total_costs = accommodation_cost + extra_expenses

# Outputs
if budget >= total_costs:
    print(f'Ivanovi will be left with {abs(total_costs - budget):.2f} leva after vacation.')
else:
    print(f'{total_costs - budget:.2f} leva needed.')

