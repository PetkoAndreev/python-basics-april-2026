# Declaration of inputs
command = input()

# Declaration of initial help variables
prime_numbers_sum = 0
non_prime_numbers_sum = 0

# Loop until we receive command "stop"
while command != 'stop':
    current_number = int(command)

    # Check for the negative numbers
    if current_number < 0:
        print('Number is negative.')
        command = input()
        continue # If we put break here - the loop will end

    # By definition numbers above 2 are prime
    is_prime = current_number >= 2

    # We check if the number with modular divide is between 2 and current_number - 1
    for divisor in range(2, current_number):
        # If we find modular divide equal to 0 - the number is NOT PRIME
        if current_number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += current_number
    else:
        non_prime_numbers_sum += current_number

    command = input()
# The output should be outside the loops, because we aim only to show final sums.
print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {non_prime_numbers_sum}')
