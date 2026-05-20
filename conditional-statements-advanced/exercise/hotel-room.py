# Declare of inputs
month = input()
number_of_nights = int(input())

price_apartment = 0
price_studio = 0
# If we do not use IN:
# if month == 'May':
#     price_apartment = 65.00
#     price_studio = 50.00
#     total_apartment_price = price_apartment * number_of_nights
#     total_studio_price = price_studio * number_of_nights
#     if 7 < number_of_nights <= 14:
#         total_studio_price -= 0.05 * total_studio_price  # 5% discount if nights are more than 7 for studio only. We limit it up to 14 nights.
#     elif number_of_nights > 14:
#         total_studio_price -= 0.3 * total_studio_price  # 30% discount if nights are more than 14 for studio only
#         total_apartment_price -= 0.1 * total_apartment_price  # 10% discount if nights are more than 14 for apartment only no matter of the month
# elif month == 'October':
#     price_apartment = 65.00
#     price_studio = 50.00
#     total_apartment_price = price_apartment * number_of_nights
#     total_studio_price = price_studio * number_of_nights
#     if 7 < number_of_nights <= 14:
#         total_studio_price -= 0.05 * total_studio_price  # 5% discount if nights are more than 7 for studio only. We limit it up to 14 nights.
#     elif number_of_nights > 14:
#         total_studio_price -= 0.3 * total_studio_price  # 30% discount if nights are more than 14 for studio only
#         total_apartment_price -= 0.1 * total_apartment_price  # 10% discount if nights are more than 14 for apartment only no matter of the month
if month in ('May', 'October'): # in => if month is equal to May, or month is equal to October
# OR example
# if month == 'May' or month == 'October' or month == 'December':
    price_apartment = 65.00
    price_studio = 50.00
    total_apartment_price = price_apartment * number_of_nights
    total_studio_price = price_studio * number_of_nights
    if 7 < number_of_nights <= 14:
        total_studio_price -= 0.05 * total_studio_price  # 5% discount if nights are more than 7 for studio only. We limit it up to 14 nights.
    elif number_of_nights > 14:
        total_studio_price -= 0.3 * total_studio_price  # 30% discount if nights are more than 14 for studio only
        total_apartment_price -= 0.1 * total_apartment_price  # 10% discount if nights are more than 14 for apartment only no matter of the month
elif month in ('June', 'September'):
    price_apartment = 68.70
    price_studio = 75.20
    total_apartment_price = price_apartment * number_of_nights
    total_studio_price = price_studio * number_of_nights
    if number_of_nights > 14:
        total_studio_price -= 0.2 * total_studio_price  # 20% discount if nights are more than 14 for studio only
        total_apartment_price -= 0.1 * total_apartment_price  # 10% discount if nights are more than 14 for apartment only no matter of the month
elif month in ('July', 'August'):
    price_apartment = 77.00
    price_studio = 76.00
    total_apartment_price = price_apartment * number_of_nights
    total_studio_price = price_studio * number_of_nights
    if number_of_nights > 14:
        total_apartment_price -= 0.1 * total_apartment_price  # 10% discount if nights are more than 14 for apartment only no matter of the month

print(f'Apartment: {total_apartment_price:.2f} lv.')
print(f'Studio: {total_studio_price:.2f} lv.')


# If month is January, February, March - season is WINTER, if April, May, June - season is Spring...
if month == 'January':
    season = 'WINTER'
elif month == 'February':
    season = 'WINTER'
elif month == 'March':
    season = 'WINTER'

if month in('January', 'February', 'March'): # IN - one variable may be in one of many values
    season = 'WINTER'


