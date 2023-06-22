class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fish)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"

    def get_animals_count(self):
        return self.__animals


zoo_name = input()
zoo = Zoo(zoo_name)
animals_count = int(input())
for animal in range(animals_count):
    current_species, current_animal = input().split()
    zoo.add_animal(current_species, current_animal)
species_type = input()
print(zoo.get_info(species_type))
print(f"Total animals: {zoo.get_animals_count()}")
