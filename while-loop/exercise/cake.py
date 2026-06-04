# Declare of inputs
cake_width = int(input())
cake_length = int(input())

# Declare help variable for the output
cake_size = cake_width * cake_length
eated_pieces = 0
input_pieces = input()  # We can receive command STOP and number of pieces of eated cake

while input_pieces != 'STOP':
    input_pieces = int(input_pieces)  # Cast number of pieces as INT
    eated_pieces += input_pieces
    if eated_pieces > cake_size:
        print(f'No more cake left! You need {eated_pieces - cake_size} pieces more.')
        break
    input_pieces = input()

if input_pieces == 'STOP':
    print(f'{abs(eated_pieces - cake_size)} pieces are left.')
