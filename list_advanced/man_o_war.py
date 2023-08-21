pirate_ship_status = [int(s) for s in input().split('>')]
warship_status = [int(s) for s in input().split('>')]
maximum_healt_capacity = int(input())

while True:
    command_info = input()
    if command_info == 'Retire':
        break

    command_info = command_info.split(' ')
    action = command_info[0]

    if action == 'Fire':
        index = int(command_info[1])
        damage = int(command_info[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
        if warship_status[index] <= 0:
            print(f'You won! The enemy ship has sunken.')
            break
    elif action == 'Defend':
        pass
    elif action == 'Repair':
        pass
    elif action == 'Status':
        pass
status = 0
print(f'Pirate ship status: {status}')
print(f'Warship status: {status}')