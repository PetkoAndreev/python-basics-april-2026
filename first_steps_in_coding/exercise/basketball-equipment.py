# Input data declaration
annual_training_basketball_fee = int(input())

# Accesories prices
basketball_shoes_price = (1 - 0.4) * annual_training_basketball_fee # 1 represents 100% from annual fee price and 0.4 represents part of the annual fee which is subtracted
basketball_outfit_price = (1 - 0.2) * basketball_shoes_price # 1 represents 100% from shoes price and 0.2 represents part of the shoes which is subtracted
basketball_ball_price = 0.25 * basketball_outfit_price # basketball_outfit_price / 4
basketball_accessories_price = basketball_ball_price / 5 # 0.20 * basketball_ball_price

total_price = annual_training_basketball_fee + basketball_shoes_price + \
              basketball_outfit_price + basketball_ball_price + \
basketball_accessories_price

print(total_price)
# Input and Output
# 365	811.76
# Вход	Изход
# 550	1223.2
