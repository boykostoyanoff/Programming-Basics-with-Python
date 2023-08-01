fires_with_sells = input().split('#')
water = int(input())
total_fire = 0
effort = 0

result = f'Cells:\n'


for fire in fires_with_sells:
    is_valid_cell = False
    fire_list = fire.split(' = ')

    if fire_list[0] == 'High' and 81 <= int(fire_list[1]) <= 125:
        is_valid_cell = True
    if fire_list[0] == 'Medium' and 51 <= int(fire_list[1]) <= 80:
        is_valid_cell = True
    if fire_list[0] == 'Low' and 1 <= int(fire_list[1]) <= 50:
        is_valid_cell = True

    if is_valid_cell and water >= int(fire_list[1]):
        water -= int(fire_list[1])
        result += f' - {fire_list[1]}\n'
        total_fire += int(fire_list[1])
        effort += int(fire_list[1]) * 0.25

print(result.rstrip('\n'))
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')