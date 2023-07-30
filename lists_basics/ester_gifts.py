gifts = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break
    command = command.split(' ')
    gift = command[1]

    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        index = int(command[-1])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command[0] == 'JustInCase':
        gifts[-1] = gift

for g in gifts:
    if not g == 'None':
        print(g, end=' ')