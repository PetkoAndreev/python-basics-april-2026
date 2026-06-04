# Declare inputs
num_tabs = int(input())
salary = int(input())

# Initial variables with defaul values
penalty = 0
facebook_penalty = 150
instagram_penalty = 100
reddit_penalty = 50

for i in range(num_tabs):
    website_name = input()
    if website_name == 'Facebook':
        penalty += facebook_penalty  # penalty = penalty + facebook_penalty
    elif website_name == 'Instagram':
        penalty += instagram_penalty
    elif website_name == 'Reddit':
        penalty += reddit_penalty

    if salary - penalty <= 0:
        print('You have lost your salary.')
        break

if salary - penalty > 0:
    print(salary - penalty)
# This is example why indentation/tabulation in Python is so important!!!
# if salary - penalty <= 0:
#     print('You have lost your salary.')
# elif salary - penalty > 0:
#     print(salary - penalty)