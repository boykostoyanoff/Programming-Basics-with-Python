group_size = int(input())
days = int(input())

coins_for_companion = 2
earned_coins_per_day = 50
my_coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    my_coins += earned_coins_per_day
    my_coins -= group_size * coins_for_companion

    if day % 3 == 0:
        my_coins -= group_size * 3

    if day % 5 == 0:
        my_coins += group_size * 20
        if day % 3 == 0:
            my_coins -= group_size * 2

print(f'{group_size} companions received {my_coins // group_size} coins each.')