# Declare inputs
lily_age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input()) # This is the price for 1 toy

saved_money = 0
toys_count = 0
birthday_money = 0 # On each odd birthday Lily gets money and her brother gets 1.00 from it
brother_money = 1 # This is the amount which brother of Lily gets from her birthday money

for birthday in range(1, lily_age + 1): # + 1 to the age to include the age, e.g. if 77 - 77 + 1 to include 77 as well
    # Check if birthday is odd or even
    if birthday % 2 == 0:
        birthday_money += 10
        saved_money += birthday_money - brother_money
    else:
        toys_count += 1

toys_money = toys_count * one_toy_price
total_money = saved_money + toys_money

difference = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
