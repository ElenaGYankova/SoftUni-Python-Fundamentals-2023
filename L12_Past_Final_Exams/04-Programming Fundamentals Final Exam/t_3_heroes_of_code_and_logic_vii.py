heroes_count = int(input())
party = {}

for num in range(heroes_count):
    hero, hit_points, mana = input().split()
    party[hero] = {"hit points": int(hit_points), "mana": int(mana)}

command = input().split(" - ")

while command[0] != "End":
    hero_name = command[1]

    if command[0] == "CastSpell":
        mana_needed, spell_name = int(command[2]), command[3]
        if party[hero_name]["mana"] >= mana_needed:
            party[hero_name]["mana"] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {party[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        party[hero_name]["hit points"] -= damage
        if party[hero_name]["hit points"] > 0:
            current_hp = party[hero_name]['hit points']
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del party[hero_name]
    elif command[0] == "Recharge":
        recharge_amount = int(command[2])
        current_mana = party[hero_name]["mana"]
        if current_mana + recharge_amount <= 200:
            amount_recovered = recharge_amount
        else:
            amount_recovered = 200 - current_mana
        party[hero_name]["mana"] += amount_recovered
        print(f"{hero_name} recharged for {amount_recovered} MP!")
    elif command[0] == "Heal":
        heal_amount = int(command[2])
        current_hit_points = party[hero_name]["hit points"]
        if current_hit_points + heal_amount <= 100:
            amount_recovered = heal_amount
        else:
            amount_recovered = 100 - current_hit_points
        party[hero_name]["hit points"] += amount_recovered
        print(f"{hero_name} healed for {amount_recovered} HP!")

    command = input().split(" - ")

for hero, info in party.items():
    print(hero)
    print(f"  HP: {party[hero]['hit points']}")
    print(f"  MP: {party[hero]['mana']}")
