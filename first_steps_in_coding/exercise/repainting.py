# Input declaration
nylon_square_meters = int(input())
paint_liters = int(input())
paint_thinner_liters = int(input())
work_hours = int(input())
# Prices of the materials
nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00
bags_price = 0.40
# Additional quantity of paint and nylon
additional_nylon_meters = 2
additional_paint_liters = paint_liters * 0.1 # 10% = 0.1
# Total prices/sums per product type
nylon_total_sum = (nylon_square_meters + additional_nylon_meters) * nylon_price
paint_total_sum = (paint_liters + additional_paint_liters) * paint_price
paint_thinner_total_sum = paint_thinner_liters * paint_thinner_price

materials_total_sum = nylon_total_sum + paint_total_sum + paint_thinner_total_sum + bags_price
workers_total_sum = (0.3 * materials_total_sum) * work_hours

final_price = materials_total_sum + workers_total_sum

print(final_price)
# 727.09
