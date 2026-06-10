# Declaration of inputs
# input_number = int(input())
#
# # Generation of all 4-digit numbers through 4 nested loops
# for first_digit in range(1, 10):
#     for second_digit in range(1, 10):
#         for third_digit in range(1, 10):
#             for fourth_digit in range(1, 10):
#                 # Check if N is modular divided to each digit
#                 is_special_number = (
#                         input_number % first_digit == 0 and
#                         input_number % second_digit == 0 and
#                         input_number % third_digit == 0 and
#                         input_number % fourth_digit == 0
#                 )
#                 if is_special_number:
#                     print(f'{first_digit}{second_digit}' \
#                           f'{third_digit}{fourth_digit}', end=' ')
# Short variant of the solution - STR + enumerate
number = int(input())
# Loop through all 4-digit numbers in interval 1111 - 9999
for current_number in range(1111, 10000):
    counter = 0
    # Loop through each digit of the current 4-digit number
    for index, digit in enumerate(str(current_number)):
        # Check if number is special
        if int(digit) != 0 and number % int(digit) == 0:
            counter += 1
    if counter == 4:
        print(current_number, end=' ')
