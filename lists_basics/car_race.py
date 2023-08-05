times_list = input().split(' ')
left_car_time = 0
right_car_time = 0

for step in range(0, len(times_list) // 2):
    time = int(times_list[step])
    if time == 0:
        left_car_time = left_car_time - 0.20 * left_car_time
    else:
        left_car_time += time

    time = int(times_list[-1 - step])
    if time == 0:
        right_car_time = right_car_time - 0.20 * right_car_time
    else:
        right_car_time += time

if left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')


