# Declare of inputs
vacation_money = float(input())
current_money = float(input())

# Declare help variable for the output
days_counter = 0
spend_days = 0

while current_money < vacation_money and spend_days < 5:
    type_action = input()
    daily_money = float(input())
    if type_action == 'spend' and daily_money >= current_money:  # If Jessi want to spend more money that she has.
        current_money = 0
        spend_days += 1
    elif type_action == 'spend' and daily_money < current_money:
        current_money -= daily_money
        spend_days += 1
    else:  # This is the case when Jessy saves money -> elif type_action == 'save'
        current_money += daily_money
        spend_days = 0  # We set spend days to 0, because of the condtion for 5 subsequent days of spending
    days_counter += 1  # We increas the total days count of some action - spend or save

if spend_days == 5:
    print(f'You can\'t save the money.\n{days_counter}')

if current_money >= vacation_money:
    print(f'You saved the money for {days_counter} days.')
