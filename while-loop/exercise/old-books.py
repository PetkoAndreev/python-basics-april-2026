# Declare inputs
# target_book = input()
# counter = 0
# Variant 1
# while True:
#     checked_book = input()
#     if checked_book == target_book:
#         print(f'You checked {counter} books and found it.')
#         break
#     if checked_book == 'No More Books':
#         print(f'The book you search is not here!\nYou checked {counter} books.')
#         break
#     counter += 1 # We are increasing the number of checked books with 1 in the end of the cycle

# Variant 2
target_book = input()
counter = 0

checked_book = input()  # We should put this before the cycle in ordet to have our first book to check
while checked_book != 'No More Books':
    if checked_book == target_book:
        print(f'You checked {counter} books and found it.')
        break
    checked_book = input()
    counter += 1 # We are increasing the number of checked books with 1 in the end of the cycle
if checked_book == 'No More Books':
    print(f'The book you search is not here!\nYou checked {counter} books.')
