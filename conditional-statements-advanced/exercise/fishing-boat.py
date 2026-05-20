# Declare of inputs
group_budget = int(input())
season = input()
number_fishermans = int(input())

# Declare default values
ship_price = 0.00

# Set conditions by season first and then by fishermans number
# This is an example of that we could use nested conditional statements, but it's not best practice and we have repeateble code
# if season == 'Spring':
#     ship_price = 3000.00
#     if number_fishermans <= 6:
#         ship_price -= 0.1 * ship_price
#     elif 7 <= number_fishermans <= 11:
#         ship_price -= 0.15 * ship_price
#     elif number_fishermans >= 12:
#         ship_price -= 0.25 * ship_price
#     if number_fishermans % 2 == 0:
#         ship_price -= 0.05 * ship_price
# elif season in('Summer', 'Autumn'):
#     ship_price = 4200.00
#     if number_fishermans <= 6:
#         ship_price -= 0.1 * ship_price
#     elif 7 <= number_fishermans <= 11:
#         ship_price -= 0.15 * ship_price
#     elif number_fishermans >= 12:
#         ship_price -= 0.25 * ship_price
#     if number_fishermans % 2 == 0 and season != 'Autumn':
#         ship_price -= 0.05 * ship_price
# elif season == 'Winter':
#     ship_price = 2600.00
#     if number_fishermans <= 6:
#         ship_price -= 0.1 * ship_price
#     elif 7 <= number_fishermans <= 11:
#         ship_price -= 0.15 * ship_price
#     elif number_fishermans >= 12:
#         ship_price -= 0.25 * ship_price
#     if number_fishermans % 2 == 0:
#         ship_price -= 0.05 * ship_price

# Set ship price
if season == 'Spring':
    ship_price = 3000.00
elif season in('Summer', 'Autumn'):
    ship_price = 4200.00
elif season == 'Winter':
    ship_price = 2600.00
# Best practice is to not have repeatable code and set it separately:
if number_fishermans <= 6:
    ship_price -= 0.1 * ship_price
elif 7 <= number_fishermans <= 11:
    ship_price -= 0.15 * ship_price
elif number_fishermans >= 12:
    ship_price -= 0.25 * ship_price

# Get the check if fishermans are even and get 5% more discount
if number_fishermans % 2 == 0 and season != 'Autumn':
    ship_price -= 0.05 * ship_price

if group_budget >= ship_price:
   print(f'Yes! You have {group_budget - ship_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(group_budget - ship_price):.2f} leva.')