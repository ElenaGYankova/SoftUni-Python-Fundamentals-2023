class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return Storage.storage
