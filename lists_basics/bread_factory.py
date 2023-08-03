initial_energy = 100
initial_coins = 100
working_day_events = input()
events = working_day_events.split('|')
my_energy = initial_energy
my_coins = initial_coins
is_bakery_rush_over = False

for event in events:
    event = event.split('-')
    number = int(event[1])

    if event[0] == 'rest':
        energy_gained = number
        if energy_gained + my_energy > initial_energy:
            energy_gained = initial_energy - my_energy

        my_energy += energy_gained
        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {my_energy}.')

    elif event[0] == 'order':
        coins_gained = number
        if my_energy < 30:
            my_energy += 50
            print(f'You had to rest!')
        else:
            my_coins += coins_gained
            my_energy -= 30
            print(f'You earned {coins_gained} coins.')

    else:
        ingredient_name = event[0]
        ingredient_price = number

        if my_coins >= ingredient_price:
            my_coins -= ingredient_price
            print(f'You bought {ingredient_name}.')
        else:
            print(f'Closed! Cannot afford {ingredient_name}.')
            is_bakery_rush_over = True

    if is_bakery_rush_over:
        break

if not is_bakery_rush_over:
    print(f'Day completed!')
    print(f'Coins: {my_coins}')
    print(f'Energy: {my_energy}')
