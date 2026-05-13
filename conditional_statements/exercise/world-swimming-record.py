# Declaration of inputs
import math

record_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_meters = float(input())

time = distance_in_meters * time_in_seconds_meters


# Check if distance is more than 15 meters
if distance_in_meters >= 15:
    # delay_in_seconds = (distance_in_meters // 15) * 12.5 # Add delay of 12.5 seconds for each 15 meters
    delay_in_seconds = math.floor(distance_in_meters / 15) * 12.5 # Alternative variant of the calculation
else:
    delay_in_seconds = 0

total_time = time + delay_in_seconds

# Check if Ivan's time is better that the record
if total_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record_seconds:.2f} seconds slower.')