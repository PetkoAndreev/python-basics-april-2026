# Declaration of inputs
start_number = int(input())
end_number = int(input())


# Loop through all numbers in the interval start to end num inclusive
for current_number in range(start_number, end_number + 1):
    # Convert the number into string to loop through each of it's digits
    number_as_text = str(current_number)
    even_positions_sums = 0
    odd_positions_sums = 0
    # Loop through each of the digits of the number
    for position, digit in enumerate(number_as_text):
        # Positions are start from 0, so 1st positio is EVEN!
        if position % 2 == 0:
            even_positions_sums += int(digit)
        else:
            odd_positions_sums += int(digit)

    if even_positions_sums == odd_positions_sums:
        print(current_number, end=' ')
