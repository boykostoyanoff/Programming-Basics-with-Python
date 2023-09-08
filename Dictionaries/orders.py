products = dict()
info = input()

while not info == 'buy':
    info = info.split(' ')
    product_name = info[0]
    product_price = info[1]
    product_quantity = int(info[2])

    if product_name in products.keys():
        product_quantity += list(products[product_name].values())[0]

    products[product_name] = {product_price:product_quantity}

    info = input()

for name, info in products.items():
    print(f'{name} -> {(float(list(info.keys())[0]) * list(info.values())[0]):.2f}')