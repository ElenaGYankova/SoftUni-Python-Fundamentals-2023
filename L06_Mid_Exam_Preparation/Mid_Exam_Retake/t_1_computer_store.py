total_sum = 0
data = input()

special = 1

while data != "special" and data != "regular":
    price = float(data)

    if price > 0:
        total_sum += price
    else:
        print("Invalid price!")

    data = input()

taxes = total_sum * 0.2

if data == "special":
    special = 0.9

if total_sum == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {(total_sum + taxes) * special:.2f}$")


# command = 0
# total = 0
# buying_parts = True
#
#
# def buying_pc(off):
#     taxes = total * 0.20
#     global buying_parts
#     if off:
#         final_price = (total + taxes) - (total + taxes) * 0.10
#     else:
#         final_price = total + taxes
#     buying_parts = False
#     if total == 0:
#         print("Invalid order!")
#     else:
#         print("Congratulations you've just bought a new computer!")
#         print(f"Price without taxes: {total:.2f}$")
#         print(f"Taxes: {taxes:.2f}$")
#         print("-----------")
#         print(f"Total price: {final_price:.2f}$")
#
#
# while buying_parts:
#     command = float(command)
#     if command >= 0:
#         total += command
#     else:
#         print("Invalid price!")
#     command = input()
#     if command == "special":
#         buying_pc(True)
#     elif command == "regular":
#         buying_pc(False)


# price_without_taxes = 0
# taxes = 0
#
#
# while True:
#     command = input()
#     if command == "special" or command == "regular":
#         break
#     command = float(command)
#     if command < 0:
#         print("Invalid price!")
#     else:
#         price_without_taxes += command
#         taxes += command * 0.20
#
# total_price = price_without_taxes + taxes
# if command == "special":
#     total_price = total_price * 0.90
#
# if total_price == 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {price_without_taxes:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price:.2f}$")


# total_price = 0
# price_without_taxes = 0
# taxes = 0
# get_discount = False
# while True:
#     command = input()
#     if command == "special":
#         get_discount = True
#         break
#     if command == "regular":
#         break
#     current_price = float(command)
#     if current_price < 0:
#         print("Invalid price!")
#     else:
#         taxes += current_price * 0.2
#         total_price += current_price * 1.2
# price_without_taxes = total_price - taxes
# if get_discount:
#     total_price *= 0.90
# if total_price == 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {price_without_taxes:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {total_price:.2f}$")
