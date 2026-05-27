import sys
# Declare inputs
number = int(input())
max_number = -sys.maxsize # System max digit
sum_numbers = 0

for i in range(number):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

difference = sum_numbers - max_number

if difference == max_number:
    print(f'Yes\nSum = {difference}')
else:
    print(f'No\nDiff = {abs(max_number - difference)}')
# вход	изход	коментари
# 7
# 3
# 4
# 1
# 1
# 2
# 12
# 1
# Yes
# Sum = 12	3 + 4 + 1 + 2 + 1 + 1 = 12

# 4
# 6
# 1
# 2
# 3
# Yes
# Sum = 6	1 + 2 + 3 = 12

# 3
# 1
# 1
# 10
# No
# Diff = 8	|10 - (1 + 1)| = 8

# 3
# 5
# 5
# 1
# No
# Diff = 1	|5 - (5 + 1)| = 1

# 3
# 1
# 1
# 1
# No
# Diff = 1