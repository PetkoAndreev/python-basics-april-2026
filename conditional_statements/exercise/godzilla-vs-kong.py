# Declaration of inputs
film_budget = float(input())
num_of_statists = int(input())
dress = float(input())
# Set decor price
decor_price = 0.1 * film_budget
# Check if there will be 10% discount of the dress
if num_of_statists > 150:
    dress_price = (num_of_statists * dress) - (0.1 * (num_of_statists * dress))
else:
    dress_price = num_of_statists * dress

# Check if decor and dress price is enough or not
if decor_price + dress_price > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {(decor_price + dress_price) - film_budget:.2f} leva more.')
else:
    print(f'''Action!
Wingard starts filming with {abs((decor_price + dress_price) - film_budget):.2f} leva left.''')
