# Declare of inputs
free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

# Declare help variable for the output
free_space_volume = free_space_width * free_space_length * free_space_height
command = input()  # Read first command or number of boxes

while command != 'Done':
    boxes_count = int(command)  # We cast number of boxes to INT
    free_space_volume -= boxes_count  # We decrease the free space with the boxes moved

    if free_space_volume <= 0:
        needed_space = abs(free_space_volume)
        print(f'No more free space! You need {needed_space} Cubic meters more.')
        break
    command = input()  # Read next command or number of boxes
else:
    print(f'{free_space_volume} Cubic meters left.')

# Above with else is equivalent to this:
# if command == 'Done':
#     print(f'{free_space_volume} Cubic meters left.')
