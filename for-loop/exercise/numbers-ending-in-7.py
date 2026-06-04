# Print numbers ending in 7 from 1 to 1 000
# Variant 1 - longest:
# for i in range(1, 1001): # 1 to 1001 just to include 1 000 in the loop
#     if i % 10 == 7:
#         print(i)

# Variant 2:
# for i in range(7, 1001, 10):
#     print(i)

# Variant 3 - comprehension
[print(i) for i in range(7, 1001, 10)]