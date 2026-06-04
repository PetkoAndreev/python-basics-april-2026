# Yard greening
square_meters = float(input())
price_per_meter = 7.61
discount_percent = 0.18 # 18 % is equal to number 0.18 (18% from 100%)
price_for_all_meters = square_meters * price_per_meter
discount_price_per_meter = discount_percent * price_for_all_meters
final_price_per_meter = price_for_all_meters - discount_price_per_meter

print(f"The final price is: {final_price_per_meter} lv.")
print(f"The discount is: {discount_price_per_meter} lv.")

# The final price is: 3432.11 lv.
# The discount is: 753.39 lv.
# The final price is: 936.03 lv.
# The discount is: 205.47 lv.

