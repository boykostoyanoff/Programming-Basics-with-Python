lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

price = 0

shield_breaks = 0
fights = 0

while fights < lost_fights_count:
    fights += 1
    if fights % 2 == 0:
        price += helmet_price

    if fights % 3 == 0:
        price += sword_price

    if fights % 6 == 0:
        price += shield_price
        shield_breaks += 1

    if shield_breaks == 2:
        shield_breaks = 0
        price += armor_price

print(f'Gladiator expenses: {price:.2f} aureus')