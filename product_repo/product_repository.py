from product_repo.product import Product


class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.owner == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f"{product.owner}: {product.quantity}\n"
        return result.strip()
