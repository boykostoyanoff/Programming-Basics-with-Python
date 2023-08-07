coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

drink_name = input()
drink_quantity = int(input())


def calculate_bill(drink_name, drink_quantity):
    bill = None
    if drink_name == 'coffee':
        bill = coffee_price * drink_quantity
    elif drink_name == 'water':
        bill = water_price * drink_quantity
    elif drink_name == 'coke':
        bill = coke_price * drink_quantity
    elif drink_name == 'snacks':
        bill = snacks_price * drink_quantity

    return bill


total_price = calculate_bill(drink_name, drink_quantity)

print(f'{total_price:.2f}')
