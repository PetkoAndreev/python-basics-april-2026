# Declaration of inputs
# first_player_eggs = int(input())
# second_player_eggs = int(input())
# first_player_wins_percentage = 0
# second_player_wins_percentage = 0
# Read the commands until player 1 or player 2 runs out of eggs or command 'End' is received
# while True:
#     command = input()
#
#     if command == 'End':
#         print(f'Player one has {first_player_eggs} eggs left.')
#         print(f'Player two has {second_player_eggs} eggs left.')
#         break
#
#     if command == 'one':
#         second_player_eggs -= 1
#     elif command == 'two':
#         first_player_eggs -= 1
#
#     # Stop the game if one of the players has no eggs left
#     if first_player_eggs == 0:
#         print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
#         break
#     elif second_player_eggs == 0:
#         print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')
#         break

# Varant two
# Declaration of inputs
first_player_eggs = int(input())
second_player_eggs = int(input())

command = input()

while command != 'End' and first_player_eggs > 0 and second_player_eggs > 0:
    if command == 'one':
        second_player_eggs -= 1
    elif command == 'two':
        first_player_eggs -= 1

    # Read the next command
    if first_player_eggs != 0 and second_player_eggs != 0:
        command = input()

if command == 'End':
    print(f'Player one has {first_player_eggs} eggs left.')
    print(f'Player two has {second_player_eggs} eggs left.')
elif first_player_eggs == 0:
    print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
elif second_player_eggs == 0:
    print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')