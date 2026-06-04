# Supplies for School - calculation
pen_packages_count = int(input())
marker_packages_count = int(input())
cleaner_liter = int(input())
discount_percentage = int(input())
# Prices
pens_price = 5.80
markers_price = 7.20
cleaner_liter_price = 1.20

# Total prices per item - additional
pens_total_price = pen_packages_count * pens_price
markers_total_price = marker_packages_count * markers_price
clenar_total_price = cleaner_liter * cleaner_liter_price

total_price_without_discount = pens_total_price + markers_total_price + clenar_total_price

discount_price = total_price_without_discount * (discount_percentage / 100)
final_price_with_discount = total_price_without_discount - discount_price

print(final_price_with_discount)