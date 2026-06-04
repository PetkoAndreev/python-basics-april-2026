# Declare of inputs
daily_steps = input()  # Important - here we receive steps as numbers, but we'll receive command "Going home" in the same variable and lines from console
# Declare help variable for the output
target_steps = 10000
current_steps = 0

while daily_steps != 'Going home':
    daily_steps = int(daily_steps)  # Cast the string of number of steps to INT, e.g. '1000' -> 1000
    current_steps += daily_steps

    if current_steps >= target_steps:
        print(f'Goal reached! Good job!')
        print(f'{current_steps - target_steps} steps over the goal!')
        break
    daily_steps = input()

if daily_steps == 'Going home':
    daily_steps = int(input())
    current_steps += daily_steps
    if current_steps >= target_steps:
        print(f'Goal reached! Good job!')
        print(f'{current_steps - target_steps} steps over the goal!')
    else:
        print(f'{abs(current_steps - target_steps)} more steps to reach goal.')
