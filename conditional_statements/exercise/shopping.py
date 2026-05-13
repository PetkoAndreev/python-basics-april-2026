# Declaration of inputs
budget = float(input())

video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_price = 250.00
# Calculate prices
total_video_cards_price = video_card_count * video_card_price
processor_price = 0.35 * total_video_cards_price # The price is for 1 pc.
ram_price = 0.10 * total_video_cards_price # The price is for 1 pc.

total_processor_price = processor_count * processor_price
total_ram_price = ram_count * ram_price

total_order_price = total_video_cards_price + total_processor_price \
                    + total_ram_price
# Check for discount
if video_card_count > processor_count:
    discount = 0.15 * total_order_price # 15% discount
else:
    discount = 0
# Calculate total order price
total_order_price -= discount # Alternative - total_order_price = total_order_price - discount
# Check the budget
if budget >= total_order_price:
    budget_left = budget - total_order_price
    print(f'You have {budget_left:.2f} leva left!')
else:
    needed_budget = abs(budget - total_order_price) # Alternative => total_order_price - budget
    print(f'Not enough money! You need {needed_budget:.2f} leva more!')
