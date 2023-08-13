targets = [int(t) for t in input().split(' ')]

while True:
    command_info = input()

    if command_info == 'End':
        print(targets)
        break
    command_info = command_info.split(' ')
    command = command_info[0]
    index = int(command_info[1])

    if command == 'Shoot':
        power = int(command_info[2])

        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command == 'Add':
        value = int(command_info[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)

    elif command == 'Strike':
        radius = int(command_info[2])

        if 0 <= index - radius and index + radius < len(targets):
            targets = targets[:index - radius] + targets[index + radius + 1]
        else:
            print('Strike missed')

