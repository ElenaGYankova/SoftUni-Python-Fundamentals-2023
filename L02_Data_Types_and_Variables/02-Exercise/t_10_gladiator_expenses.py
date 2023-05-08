lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken = lost_battles // 2
sword_broken = lost_battles // 3
shield_broken = lost_battles // 6
armor_broken = shield_broken // 2

repair_expenses = helmet_broken * helmet_price + sword_broken * sword_price + \
                  shield_broken * shield_price + armor_broken * armor_price

print(f'Gladiator expenses: {repair_expenses:.2f} aureus')

'''
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_count = 0
for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if (fight % 2 == 0) and (fight % 3 == 0):
        expenses += shield_price
        shield_count += 1
    if shield_count == 2:
        expenses += armor_price
        shield_count = 0
print(f"Gladiator expenses: {expenses:.2f} aureus")
'''

'''
count_lose_battles = int(input())
price_per_one_helmet = float(input())
price_per_one_sword = float(input())
price_per_one_shield = float(input())
price_per_one_armour = float(input())
expenses = 0
counter = 0
for lose in range(1, count_lose_battles + 1):
    if lose % 2 == 0:
        expenses += price_per_one_helmet
    if lose % 3 == 0:
        expenses += price_per_one_sword
    if lose % 2 == 0 and lose % 3 == 0:   # if lose % 6 == 0:
        expenses += price_per_one_shield
        counter += 1
        if counter == 2:
            expenses += price_per_one_armour
            counter = 0
        else:
            continue
print(f"Gladiator expenses: {expenses:.2f} aureus")
'''

# count_lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armour_price = float(input())
# count_helmets = count_lost_fights // 2
# count_swords = count_lost_fights // 3
# count_shields = count_lost_fights // 6   # count_lost_fights // (2 * 3)
# count_armours = count_shields // 2
# expenses_per_helmets = count_helmets * helmet_price
# expenses_per_swords = count_swords * sword_price
# expenses_per_shields = count_shields * shield_price
# expenses_per_armours = count_armours * armour_price
# total_expenses = expenses_per_helmets + expenses_per_swords + expenses_per_shields + expenses_per_armours
# print(f"Gladiator expenses: {total_expenses:.2f} aureus")


# count_failed_battles = int(input())
# price_per_one_helmet = float(input())
# price_per_one_sword = float(input())
# price_per_one_shield = float(input())
# price_per_one_armour = float(input())
# expenses = 0
# count_broken_shield = 0
# for failed_battle in range(1, count_failed_battles + 1):
#     if failed_battle % 2 == 0:
#         expenses += price_per_one_helmet
#     if failed_battle % 3 == 0:
#         expenses += price_per_one_sword
#     if failed_battle % 2 == 0 and failed_battle % 3 == 0:
#         expenses += price_per_one_shield
#         count_broken_shield += 1
#         if count_broken_shield == 2:
#             expenses += price_per_one_armour
#             count_broken_shield = 0
#         else:
#             continue
# print(f"Gladiator expenses: {expenses:.2f} aureus")



################################################   Task Description   ################################################
# 10. * Gladiator Expenses
# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. 
# His equipment consists of a helmet, a sword, a shield, and an armor. 
# You will receive Peter's lost fights count. 
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired. 
# You will receive the price of each item in his equipment. 
# Calculate his expenses for the year for renewing his equipment. 
# Input / Constraints
# The input will consist of 5 lines:
# • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000]. 
# • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000]. 
# • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000]. 
# • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000]. 
# Output
# • As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
