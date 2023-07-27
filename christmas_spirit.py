quantity_of_decoration = int(input())
days_left = int(input())

total_cost = 0
total_spirit = 0
days_passed = 0

ornament_price = 2
ornament_points = 5

skirt_price = 5
skirt_points = 3

garland_price = 3
garland_points = 10

lights_price = 15
lights_points = 17

while days_left > 0:
    days_left -= 1
    days_passed += 1

    if days_passed % 11 == 0:
        quantity_of_decoration += 2

    if days_passed % 2 == 0:
        total_cost += ornament_price * quantity_of_decoration
        total_spirit += ornament_points

    if days_passed % 3 == 0:
        total_cost += (skirt_price + garland_price) * quantity_of_decoration
        total_spirit += skirt_points + garland_points

    if days_passed % 5 == 0:
        total_cost += lights_price * quantity_of_decoration
        total_spirit += lights_points

    if days_passed % 3 == 0 and days_passed % 5 == 0:
        total_spirit += 30

    if days_passed % 10 == 0:
        total_spirit -= 20

        total_cost += skirt_price + garland_price + lights_price

if days_passed % 10 == 0:
    total_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
