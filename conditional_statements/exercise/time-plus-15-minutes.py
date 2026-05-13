# Declaration of inputs
hour = int(input())
minute = int(input())

# Check for minutes
if minute >= 45:
    minute = (minute + 15) - 60 # 45 + 15 = 60 - 1 hour. We need to set minutes = 0 and increase hour with 1
    hour = hour + 1
else:
    minute = minute + 15

# Check for the hour if 24
if hour == 24:
    hour = 0

# Set leading 0 to the minutes
if minute < 10:
    print(f'{hour}:0{minute}')
else:
    print(f'{hour}:{minute}')