budget = float(input())
flour_price = float(input())

loaves = 0
colored_eggs = 0

eggs_price = 0.75 * flour_price
milk_price = flour_price * 1.25 / 4

one_bread_price = flour_price + eggs_price + milk_price

while budget >= one_bread_price:
    budget -= one_bread_price
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')