# Declare of inputs
type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

# Declare flowers prices
rose_price = 5.00
dahila_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50

final_price = 0

if type_of_flowers == 'Roses':
    final_price = number_of_flowers * rose_price
    if number_of_flowers > 80:
        final_price = final_price - (0.1 * final_price)  # 0.1 is the equuivalent of 10%
        # final_price -= 0.1 * final_price
elif type_of_flowers == 'Dahlias':
    final_price = number_of_flowers * dahila_price
    if number_of_flowers > 90:
        final_price -= 0.15 * final_price
elif type_of_flowers == 'Tulips':
    final_price = number_of_flowers * tulip_price
    if number_of_flowers > 80:
        final_price -= 0.15 * final_price
elif type_of_flowers == 'Narcissus':
    final_price = number_of_flowers * narcissus_price
    if number_of_flowers < 120:
        final_price += 0.15 * final_price
elif type_of_flowers == 'Gladiolus':
    final_price = number_of_flowers * gladiolus_price
    if number_of_flowers < 80:
        final_price += 0.20 * final_price

if budget < final_price:  # Case when budget is not enough
    print(f'Not enough money, you need {final_price - budget:.2f} leva more.')
else:  # In all other cases the budget will be enough
    print(
        f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {budget - final_price:.2f} leva left.')
