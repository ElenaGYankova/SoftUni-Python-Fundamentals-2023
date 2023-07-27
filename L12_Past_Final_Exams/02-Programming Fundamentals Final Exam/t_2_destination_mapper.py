import re

text = input()
pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, text)
destinations = [x[1] for x in matches]
travel_points = sum([len(destination) for destination in destinations])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
