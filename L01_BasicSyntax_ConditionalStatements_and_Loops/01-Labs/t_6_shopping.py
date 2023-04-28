budget = int(input())

while True:
    product_price = input()
    if product_price != "End":
        product_price = int(product_price)
        if product_price > budget:
            print(f"You went in overdraft!")
            break
        budget -= product_price
    else:
        print("You bought everything needed.")
        break

'''
budget = int(input())

command = input()
while command != "End":
    product_price = int(command)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
'''

'''
budget = int(input())
total_sum = 0
command = input()
money_is_enough = True
while command != "End":
    product_price = int(command)
    total_sum += product_price
    if budget < total_sum:
        print("You went in overdraft!")
        money_is_enough = False
        break
    command = input()
if money_is_enough:
    print("You bought everything needed.")
'''

######   Task Description   ###### 6. Shopping
# Write a program that reads an integer number representing a budget.
# On the following lines, it reads integer numbers 
# representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, 
# it prints "You went in overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."
