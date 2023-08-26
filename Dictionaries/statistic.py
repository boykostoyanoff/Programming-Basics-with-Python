products = {}

while True:
    data = input()
    if data == 'statistics':
        break

    data = data.split(': ')
    if data[0] in products.keys():
        data[1] = int(data[1]) + products[data[0]]

    products[data[0]] = int(data[1])


print("Products in stock:")
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')