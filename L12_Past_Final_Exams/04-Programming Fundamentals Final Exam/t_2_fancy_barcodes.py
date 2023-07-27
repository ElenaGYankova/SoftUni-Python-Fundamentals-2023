import re

count = int(input())
validation_pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"

for _ in range(count):
    barcode = input()
    validation = re.search(validation_pattern, barcode)

    if validation:
        current_barcode = validation.group()
        code_pattern = r"\d+"
        match = re.findall(code_pattern, current_barcode)
        if match:
            product_group = "".join(match)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")

    else:
        print("Invalid barcode")
