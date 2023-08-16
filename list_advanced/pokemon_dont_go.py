distances = [int(d) for d in input().split(' ')]
total_score = 0

while distances:
    index = int(input())
    index_value = ''

    if index < 0:
        total_score += distances[0]
        index_value = distances[0]
        distances[0] = distances[-1]
    elif index >= len(distances):
        total_score += distances[-1]
        index_value = distances[-1]
        distances[-1] = distances[0]
    else:
        index_value = distances[index]
        total_score += index_value
        distances.pop(index)

    if distances:
        distances = [el + index_value if el <= index_value else el - index_value for el in distances]

print(total_score)