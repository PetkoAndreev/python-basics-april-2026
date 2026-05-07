# Inputs declaration
chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())
# Menu items prices
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
# Total price per menu
chicken_menu_total_price = chicken_menus_count * chicken_menu_price
fish_menu_total_price = fish_menus_count * fish_menu_price
vegetarian_menu_total_price = vegetarian_menus_count * vegetarian_menu_price

food_total_price = chicken_menu_total_price + fish_menu_total_price + vegetarian_menu_total_price
dessert_price = 0.2 * food_total_price
delivery_price = 2.50

order_total_price = food_total_price + dessert_price + delivery_price
print(order_total_price)