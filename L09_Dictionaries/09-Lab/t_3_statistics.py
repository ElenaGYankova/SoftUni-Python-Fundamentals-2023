bakery_stock = {}
command = input()

while command != "statistics":
    current_key, current_value = command.split(": ")

    if current_key in bakery_stock:
        bakery_stock[current_key] += int(current_value)
    else:
        bakery_stock[current_key] = int(current_value)
    command = input()

print("Products in stock:")

for (key, value) in bakery_stock.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(bakery_stock)}")
print(f"Total Quantity: {sum(bakery_stock.values())}")
