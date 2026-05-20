# Declare of inputs
budget = float(input())
season = input()

# Declare initial values of variables
destination = ''
type_vacation = ''
budget_spend = 0

# Get the conditiona statements:
# Step 1 - define by season
# Step 2 - checks by the budget
if season == 'summer':
    if budget <= 100:
        destination = 'Bulgaria'
        type_vacation = 'Camp'
        budget_spend = 0.3 * budget  # 30% spend of the budget in Bulgaria
    elif budget <= 1000:
        destination = 'Balkans'
        type_vacation = 'Camp'
        budget_spend = 0.4 * budget  # 40% spend of the budget in Balkans
    else: # Alternative elif budget > 1000
        destination = 'Europe'
        type_vacation = 'Hotel'
        budget_spend = 0.9 * budget  # 90% spend of the budget in Europe
elif season == 'winter':
    type_vacation = 'Hotel'  # No matter of the destination in Winter it's always on a hotel.
    if budget <= 100:
        destination = 'Bulgaria'
        budget_spend = 0.7 * budget  # 70% spend of the budget in Bulgaria
    elif budget <= 1000:
        destination = 'Balkans'
        budget_spend = 0.8 * budget  # 80% spend of the budget in Balkans
    else:
        destination = 'Europe'
        budget_spend = 0.9 * budget  # 90% spend of the budget in Europe

print(f'Somewhere in {destination}')
print(f'{type_vacation} - {budget_spend:.2f}')
