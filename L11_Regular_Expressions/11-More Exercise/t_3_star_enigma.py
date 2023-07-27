import re

number_of_messages = int(input())
attacked_planets = []
destroyed_planets = []

for message in range(number_of_messages):
    current_message = input()
    encryption_pattern = r"[SsTtAaRr]"
    decryption_key = len(re.findall(encryption_pattern, current_message))
    decrypted_message = ""
    for symbol in current_message:
        decrypted_message += chr(ord(symbol) - decryption_key)
    validation_pattern = r"@[A-Za-z]+[^@\-\!\:\>]*\:\d+[^@\-\!\:\>]*\![AD]\![^@\-\!\:\>]*\-\>\d+"
    validation = re.findall(validation_pattern, decrypted_message)

    if validation:
        name_pattern = r"@[A-Za-z]+"
        attack_pattern = r"\![AD]\!"
        planet_name = re.findall(name_pattern, decrypted_message)[0][1:]
        attack_type = re.findall(attack_pattern, decrypted_message)[0][1]
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")

if len(attacked_planets) > 0:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")

if len(destroyed_planets) > 0:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")
