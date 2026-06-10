# Declaration of inputs
movie_name = input()

# Initial help variables - counter
total_tickets_count = 0
student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0

# Loop movies until command Finish
while movie_name != 'Finish':
    # Read cinema hall capacity
    available_seats = int(input())
    # Count of sold tickets for the current movie
    current_movie_tickets_count = 0

    ticket_type = input()
    while ticket_type != 'End':
        current_movie_tickets_count += 1
        total_tickets_count += 1

        # Increase tickets by type
        if ticket_type == 'student':
            student_tickets_count += 1
        elif ticket_type == 'standard':
            standard_tickets_count += 1
        elif ticket_type == 'kid':
            kid_tickets_count += 1

        # Check if the available seats are full
        if current_movie_tickets_count == available_seats:
            break
        # Read next ticket type
        ticket_type = input()
    # Check in judge if we need to format the numbers
    cinema_hall_occupancy_percentage = current_movie_tickets_count / available_seats * 100
    print(f'{movie_name} - {cinema_hall_occupancy_percentage:.2f}% full.')
    # Read next movie title
    movie_name = input()

# Calculate percentage for each ticket type
student_tickets_percentage = student_tickets_count / total_tickets_count * 100
standard_tickets_percentage = standard_tickets_count / total_tickets_count * 100
kid_tickets_percentage = kid_tickets_count / total_tickets_count * 100

print(f'Total tickets: {total_tickets_count}')
print(f'{student_tickets_percentage:.2f}% student tickets.')
print(f'{standard_tickets_percentage:.2f}% standard tickets.')
print(f'{kid_tickets_percentage:.2f}% kids tickets.')
