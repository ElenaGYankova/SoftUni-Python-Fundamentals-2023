def calculate_price(product, quantity):
    product_price = 0
    if product == "coffee":
        product_price = 1.50
    elif product == "water":
        product_price = 1.00
    elif product == "coke":
        product_price = 1.40
    elif product == "snacks":
        product_price = 2.00
    return f"{(product_price * quantity):.2f}"


input_product = input()
input_quantity = int(input())
print(calculate_price(input_product, input_quantity))
