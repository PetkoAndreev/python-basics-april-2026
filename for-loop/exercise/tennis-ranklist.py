# Declare inputs
tournaments_count = int(input())
starting_points = int(input())

final_points = starting_points
earned_points = 0  # This will be the points from all tournaments
won_tournaments_count = 0

win_points = 2000
finalist_points = 1200
semi_finalist_points = 720

for _ in range(tournaments_count):
    tournament_stage = input()

    if tournament_stage == 'W':
        earned_points += win_points
        won_tournaments_count += 1  # Increase number of won tournaments
    elif tournament_stage == 'F':
        earned_points += finalist_points
    elif tournament_stage == 'SF':
        earned_points += semi_finalist_points

final_points += earned_points
average_points = earned_points // tournaments_count # To check if this rounds up to lowest whole number
won_tournaments_percentage = won_tournaments_count / tournaments_count * 100

# Output
print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{won_tournaments_percentage:.2f}%')
