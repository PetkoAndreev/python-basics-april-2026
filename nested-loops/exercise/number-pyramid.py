# Declaration of inputs
max_number = int(input())

current_number_to_print = 1
is_number_bigger_than_max = False

# Outside loop for rows
for row in range(1, max_number + 1):
    # Inner loop - define how many numbers we have at the current row
    for column in range(1, row + 1):
        # If we overtake max_number
        if current_number_to_print > max_number:
            is_number_bigger_than_max = True
            break
        print(current_number_to_print, end=' ')
        current_number_to_print += 1
    if is_number_bigger_than_max:
        break

    print() # It prints empty row
