rooms = int(input())
free_chairs = 0
is_game_on = True

for i in range(1, rooms + 1):
    chairs_info = input().split(' ')
    chairs = len(chairs_info[0])
    used_chairs = int(chairs_info[1])
    if used_chairs > chairs:
        print(f'{used_chairs - chairs} more chairs needed in room {i}')
        is_game_on = False
    free_chairs += chairs - used_chairs

if is_game_on:
    print(f'Game On, {free_chairs} free chairs left')