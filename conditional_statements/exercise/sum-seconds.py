# Declaration of inputs
time_first_seconds = int(input())
time_second_seconds = int(input())
time_third_seconds = int(input())

total_time_in_seconds = time_first_seconds + time_second_seconds + time_third_seconds

minutes = total_time_in_seconds // 60 # Here we calculate the minutes
seconds = total_time_in_seconds % 60 # Here we calculate the seconds left

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')