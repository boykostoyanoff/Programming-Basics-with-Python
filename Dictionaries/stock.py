data = input()
data = data.split(' ')
products_dict = {}

for p in range(0, len(data), 2):
    products_dict[data[p]] = data[p + 1]

products = input().split(' ')
for product in products:
    if product in products_dict.keys():
        print(f'We have {products_dict[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")