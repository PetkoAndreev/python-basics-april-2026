# Declaration of inputs
initial_points = int(input())
bonus = 0
# Initial bonus, based on the points
if initial_points <= 100:
    bonus = 5
elif initial_points <= 1000: # Alternative - initial_points > 100 and initial_points <= 1000
    bonus = 0.2 * initial_points # 20% is 0.2 for ease
else:
    bonus = 0.1 * initial_points # 10% is 0.1 for ease

# Additional bonus points
if initial_points % 2 == 0: # Check if odd number
    bonus = bonus + 1
elif initial_points % 10 == 5: # Check in number ends with 5
    bonus = bonus + 2

print(bonus)
print(f'{initial_points + bonus}')

