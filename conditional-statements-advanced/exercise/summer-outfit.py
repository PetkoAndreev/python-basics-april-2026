# Declare of inputs
degrees = int(input())
day_time = input()
# Declare intial variable with default value
outfit = ''
shoes = ''

# Step 1 - define if condition by day time - Morning, Afternoon and Evening
# Step 2 - define sub if conditions by degrees
# if day_time == 'Morning':
#     if 10 <= degrees <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif 18 < degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif degrees >= 25:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
# elif day_time == 'Afternoon':
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < degrees <= 24:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     elif degrees >= 25:
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
# elif day_time == 'Evening':
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif degrees >= 25:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# Variant 2 - without nested conditionas statements
if day_time == 'Morning' and 10 <= degrees <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif day_time == 'Morning' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif day_time == 'Morning' and degrees >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif day_time == 'Afternoon' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif day_time == 'Afternoon' and 18 < degrees <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif day_time == 'Afternoon' and degrees >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
elif day_time == 'Evening' and 10 <= degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif day_time == 'Evening' and 18 < degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif day_time == 'Evening' and degrees >= 25:
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")