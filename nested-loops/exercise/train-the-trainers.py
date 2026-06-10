# Declaration of inputs
jury_members_count = int(input())

# Initial help variables
all_grades_sum = 0
all_grades_count = 0

# Read the first presentation
presentation_name = input()

# Read presentations + grades until command Finish
while presentation_name != 'Finish':
    # Sum of the current presentation grades
    presentation_grades_sum = 0

    # Read all the grades from the jury and loop them
    for current_jury_member in range(jury_members_count):
        current_grade = float(input())
        presentation_grades_sum += current_grade
        all_grades_sum += current_grade
        all_grades_count += 1

    # Calculate average grade for the current presentation
    average_presentation_grade = presentation_grades_sum / jury_members_count

    print(f'{presentation_name} - {average_presentation_grade:.2f}.')

    # Read next presentation name
    presentation_name = input()

# Calculate final average grade
final_average_grade = all_grades_sum / all_grades_count

print(f'Student\'s final assessment is {final_average_grade:.2f}.')
