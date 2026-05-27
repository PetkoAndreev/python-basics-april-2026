# Declare inputs
groups_count = int(input())

# Variables with initial default values
musala_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

total_climbers = 0

for _ in range(groups_count):
    current_group_size = int(input()) # Number of climbers in a particular group

    total_climbers += current_group_size # Increase the total number of climbers with each new group

    if current_group_size <= 5:
        musala_climbers += current_group_size
    elif 6 <= current_group_size <= 12:
        mont_blanc_climbers += current_group_size
    elif current_group_size <= 25:
        kilimanjaro_climbers += current_group_size
    elif current_group_size <= 40:
        k2_climbers += current_group_size
    else:
        everest_climbers += current_group_size

# Calculate percentages
musala_perc = musala_climbers / total_climbers * 100
mont_blanc_perc = mont_blanc_climbers / total_climbers * 100
kilimanjaro_perc = kilimanjaro_climbers / total_climbers * 100
k2_perc = k2_climbers / total_climbers * 100
everest_perc = everest_climbers / total_climbers * 100

print(f'''{musala_perc:.2f}%
{mont_blanc_perc:.2f}%
{kilimanjaro_perc:.2f}%
{k2_perc:.2f}%
{everest_perc:.2f}%''')