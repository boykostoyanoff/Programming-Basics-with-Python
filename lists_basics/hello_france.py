train_ticket = 150
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
separator = '|'
my_collection_budget = list()

collection = input().split(separator)
budget = float(input())

for item_info in collection:
    item_name = item_info.split('->')[0]
    item_price = float(item_info.split('->')[1])

    if item_name == 'Clothes' and 0 < item_price <= clothes_max_price or \
            item_name == 'Shoes' and 0 < item_price <= shoes_max_price or \
            item_name == 'Accessories' and 0 < item_price <= accessories_max_price:
        if budget >= item_price:
            budget -= item_price
            my_collection_budget.append(item_price)

for price in my_collection_budget:
    print(f'{(price * 1.4):.2f}', end=' ')
print()
print(f'Profit: {(sum(my_collection_budget) * 0.4):.2f}')

if budget + sum(my_collection_budget) * 1.4 >= train_ticket:
    print('Hello, France!')
else:
    print(f'Not enough money.')