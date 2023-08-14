days_of_adventure = int(input())
the_n_of_players = int(input())
amount_of_energy = float(input())
water_for_day = float(input())
food_for_day = float(input())

total_water = days_of_adventure * the_n_of_players * water_for_day
total_food = days_of_adventure * the_n_of_players * food_for_day

is_no_energy = False
for day in range(1, days_of_adventure + 1):
    energy_lost = float(input())
    if amount_of_energy > energy_lost:
        amount_of_energy -= energy_lost
    else:
        is_no_energy = True
        break
    if day % 2 == 0:
        amount_of_energy += amount_of_energy * 0.05
        total_water -= total_water * 0.3
    if day % 3 == 0:
        total_food -= total_food / the_n_of_players
        amount_of_energy += amount_of_energy * 0.1

if is_no_energy:
    print(f"You will run out of energy. You will be left with"
          f" {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with"
          f" - {amount_of_energy:.2f} energy!")
