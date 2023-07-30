deck = input().split(' ')
shuffles = int(input())
result = list()

for j in range(shuffles):
    result = [deck[0]]
    for i in range(1, len(deck) // 2):
        result.append(deck[i + len(deck) // 2 - 1])
        result.append(deck[i])

    result.append(deck[-1])
    deck = list()
    for j in result:
        deck.append(j)
else:
    print(result)