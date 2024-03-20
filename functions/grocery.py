def grocery_store(**items):
    store_sorted = dict(sorted(items.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ""
    for product, quantity in store_sorted.items():
        result += f"{product}: {quantity}\n"

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
