# Declare of inputs
screening_type = input() # By default this is string (str)
rows = int(input())
columns = int(input())

# Declare variable with default values
total_tickets_price = 0
premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00
hall_size = rows * columns

if screening_type == 'Premiere':
    total_tickets_price = hall_size * premiere_price
elif screening_type == 'Normal':
    total_tickets_price = hall_size * normal_price
elif screening_type == 'Discount':
    total_tickets_price = hall_size * discount_price

print(f'{total_tickets_price:.2f} leva')