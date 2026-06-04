# Declare of inputs
number_of_bad_grades = int(input())
task_name = input()
task_grade = int(input())

# Declare help variable for the output
tasks_counter = 0
tasks_sum_grades = 0
tasks_bad_grades_count = 0
previous_task_name = ''

# Write our while loop
while task_name != 'Enough':
    if task_grade <= 4:
        tasks_bad_grades_count += 1
    if tasks_bad_grades_count == number_of_bad_grades:
        print(f'You need a break, {tasks_bad_grades_count} poor grades.')
        break
    tasks_counter += 1
    tasks_sum_grades += task_grade
    previous_task_name = task_name

    task_name = input()
    if task_name == 'Enough':
        average_grade = tasks_sum_grades / tasks_counter
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {tasks_counter}')
        print(f'Last problem: {previous_task_name}')
    else:
        task_grade = int(input())