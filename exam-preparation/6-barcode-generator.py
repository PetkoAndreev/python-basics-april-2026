# # Declaration of inputs
# start_number = input()
# end_number = input()
#
# # Take each digit separately - work with string indexes
# start_first_digit = int(start_number[0])
# start_second_digit = int(start_number[1])
# start_third_digit = int(start_number[2])
# start_fourth_digit = int(start_number[3])
#
# end_first_digit = int(end_number[0])
# end_second_digit = int(end_number[1])
# end_third_digit = int(end_number[2])
# end_fourth_digit = int(end_number[3])
#
# # Generate all barcodes with odd digits
# for first_digit in range(start_first_digit, end_first_digit + 1):
#     for second_digit in range(start_second_digit, end_second_digit + 1):
#         for third_digit in range(start_third_digit, end_third_digit + 1):
#             for fourth_digit in range(start_fourth_digit, end_fourth_digit + 1):
#                 if (
#                     first_digit % 2 != 0
#                     and second_digit % 2 != 0
#                     and third_digit % 2 != 0
#                     and fourth_digit % 2 != 0
#                 ):
#                     print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')

start_number = input()
end_number = input()

for current_number in range(int(start_number), int(end_number) + 1):
    current_number_as_text = str(current_number) # To use it in enumerate
    valid_digits_count = 0

    # Check whether every digit is odd and inside the positional range
    for index, digit in enumerate(current_number_as_text):
        start_digit = int(start_number[index]) # First digit from first number, second digit, etc.
        end_digit = int(end_number[index]) # First digit from second number, second digit, etc.
        current_digit = int(digit)

        if start_digit <= current_digit <= end_digit and current_digit % 2 != 0:
            valid_digits_count += 1

    # Print only valid barcodes
    if valid_digits_count == 4:
        print(current_number, end=' ')