class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        result = list()
        for pr in self.products:
            if pr[0] == letter:
                result.append(pr)
        return result

    def __repr__(self):

        repr_string = f'Items in the {self.name} catalogue:\n'
        for item in sorted(self.products):
            repr_string += f'{item}\n'
        return repr_string.rstrip('\n')


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)