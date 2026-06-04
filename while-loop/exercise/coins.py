# Declare of inputs
# change = float(input())

# Declare help variable for the output
# num_coins = 0  # We need it for the output

# While our change is greater than 0 we do the check for the different coins, starting from the biggest one
# while change != 0:
#     if change >= 2:
#         change = round(change - 2, 2)
#         num_coins += 1
#     elif change >= 1:
#         change = round(change - 1, 2)
#         num_coins += 1
#     elif change >= 0.50:
#         change = round(change - 0.50, 2)
#         num_coins += 1
#     elif change >= 0.20:
#         change = round(change - 0.20, 2)
#         num_coins += 1
#     elif change >= 0.10:
#         change = round(change - 0.10, 2)
#         num_coins += 1
#     elif change >= 0.05:
#         change = round(change - 0.05, 2)
#         num_coins += 1
#     elif change >= 0.02:
#         change = round(change - 0.02, 2)
#         num_coins += 1
#     elif change >= 0.01:
#         change = round(change - 0.01, 2)
#         num_coins += 1
#
# print(num_coins)

# Variant 2 - FOR loop - shorter
# We will convert the change into coins
change_in_coins = round(float(input()) * 100)

# We will use LIST - which is not yet learned
coins = [200, 100, 50, 20, 10, 5, 2, 1]

num_coins = 0

for coin in coins:
    num_coins += change_in_coins // coin
    change_in_coins %= coin

print(num_coins)