class Shop:
    SMALL_SHOP_CAPACITY = 10

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name: str, type: str):
        return Shop(name, type, cls.SMALL_SHOP_CAPACITY)

    def add_item(self, item_name: str):
        items_in_shop = sum(self.items.values())
        if self.capacity == items_in_shop:
            return f"Not enough capacity in the shop"
        if item_name in self.items.keys():
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        for item, quantity in self.items.items():
            if item == item_name:
                if quantity >= amount:
                    self.items[item_name] -= amount
                    if self.items[item_name] == 0:
                        self.items.pop(item_name)
                    return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
