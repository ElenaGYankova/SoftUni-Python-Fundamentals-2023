command = input()
products = {}

while not command == 'buy':
    name, price, quantity = command.split()
    if name not in products:
        products[name] = [float(price), int(quantity)]
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)
    command = input()

for key in products:
    print(f'{key} -> {(products[key][0] * products[key][1]):.2f}')
