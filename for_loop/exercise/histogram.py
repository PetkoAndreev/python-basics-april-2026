# Declare inputs
number_iterations = int(input())

# Long option
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
# Short option
p1 = p2 = p3 = p4 = p5 = 0 # We say all 5 variable has initial value 0

for _ in range(number_iterations):
    current_number = int(input())

    if current_number < 200:
        p1 += 1 # We have one more number in this range
    elif current_number < 400: # This is equivelent of between 201 and 399 => 200 < current_number <= 399
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    else: # elif current_number >= 800
        p5 += 1
# Calculate percentages

p1_perc = p1 / number_iterations * 100
p2_perc = p2 / number_iterations * 100
p3_perc = p3 / number_iterations * 100
p4_perc = p4 / number_iterations * 100
p5_perc = p5 / number_iterations * 100

print(f'''{p1_perc:.2f}%
{p2_perc:.2f}%
{p3_perc:.2f}%
{p4_perc:.2f}%
{p5_perc:.2f}%''')