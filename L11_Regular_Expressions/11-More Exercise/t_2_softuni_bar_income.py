import re

total_income = 0
line = input()

while line != "end of shift":
    pattern = r"(%[A-Z]{1}[a-z]+\%)([^\|\$\%\.])*(<[\w]+>)([^\|\$\%\.])*(\|\d+\|)([^\|\$\%\.])*(\d+(\.\d+)*\$)"
    validation = re.findall(pattern, line)
    if validation:
        name_pattern = r"%([A-Z]{1}[a-z]+)\%"
        product_pattern = r"<([\w]+)>"
        count_pattern = r"\|(\d+)\|"
        price_pattern = r"(\d+(\.\d+)*)\$"
        name = re.findall(name_pattern, line)[0]
        product = re.findall(product_pattern, line)[0]
        count = int(re.findall(count_pattern, line)[0])
        price = float(re.findall(price_pattern, line)[0][0])
        cost = count * price
        print(f"{name}: {product} - {cost:.2f}")
        total_income += cost
    line = input()

print(f"Total income: {total_income:.2f}")
