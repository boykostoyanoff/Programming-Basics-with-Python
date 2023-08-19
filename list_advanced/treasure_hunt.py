treasure_chest = input().split('|')

while True:
    command = input().split(' ')
    if command[0] == 'Yohoho!':
        break
    if command[0] == 'Loot':
        for i in range(1, len(command)):
            treasure_item = command[i]
            if treasure_item not in treasure_chest:
                treasure_chest.insert(0, treasure_item)
    elif command[0] == 'Drop':
        index = int(command[1])
        if index in range(len(treasure_chest)):
            treasure_chest.append(treasure_chest.pop(index))
    elif command[0] == 'Steal':
        count = int(command[1])
        stolen_items = list()
        for i in range(count):
            if treasure_chest:
                stolen_items.append(treasure_chest.pop())
        print(', '.join(stolen_items[::-1]))

if treasure_chest:
    avg_treasure = sum([len(x) for x in treasure_chest]) / len(treasure_chest)
    print(f'Average treasure gain: {avg_treasure:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')