forces = {}


def add_user_to_side(name, side):
    for users in forces.values():
        if name in users:
            return
    forces[side] = forces.get(side, []) + [name]


def switch_side(side, name):
    for sides_, users in forces.items():
        if name in users:
            forces[sides_].remove(name)
            break
    forces[side] = forces.get(side, []) + [name]
    print(f"{name} joins the {side} side!")


command = input()

while command != "Lumpawaroo":
    if "|" in command:
        side, name = command.split(" | ")
        add_user_to_side(name, side)
    elif "->" in command:
        side, name = command.split(" -> ")
        switch_side(name, side)

    command = input()

for side, members in forces.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for user in members:
            print(f"! {user}")
