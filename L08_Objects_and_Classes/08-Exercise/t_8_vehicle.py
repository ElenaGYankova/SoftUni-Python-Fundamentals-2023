class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price:
            if self.owner is None:
                self.owner = owner
                change = money - self.price
                return f"Successfully bought a {self.type}. Change: {change:.2f}"
            return "Car already sold"
        return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"
