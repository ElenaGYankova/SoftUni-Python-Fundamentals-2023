class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [x for x in self.products if x[0] == first_letter]

    def __repr__(self):
        return f"Items in the {self.name} catalogue:" + "\n" + "\n".join(sorted(self.products))
