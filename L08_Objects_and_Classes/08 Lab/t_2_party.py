class Party:
    def __init__(self):
        self.people = []


party = Party()  # като party е обект
name = input()
while name != "End":
    party.people.append(name)
    name = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
