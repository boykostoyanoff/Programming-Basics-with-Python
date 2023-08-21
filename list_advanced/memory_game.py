elements = input().split(' ')
moves = 0
while True:
    twins = input()
    if twins == 'end':
        break
    moves += 1
    first_index, second_index = [int(i) for i in twins.split(' ')]

    if first_index == second_index or not 0 <= first_index < len(elements) or not 0 <= second_index < len(elements):
        element_for_insert = f'-{moves}a'
        elements.insert(len(elements) // 2, element_for_insert)
        elements.insert(len(elements) // 2, element_for_insert)
        print(f'Invalid input! Adding additional elements to the board')
        continue
    if first_index > second_index:
        first_index, second_index = second_index, first_index
    if elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements.pop(second_index)
        elements.pop(first_index)
    else:
        print(f"Try again!")
    if not elements:
        print(f"You have won in {moves} turns!")
        break
if elements:
    print(f'Sorry you lose :(')
    print(' '.join(elements))


