animals = input()

animals_list = animals.split(", ")
number_of_animals = len(animals_list)
animals_list_reversed = list(reversed(animals_list))

if animals_list_reversed[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index in range(number_of_animals):
        current_animal = animals_list_reversed[index]
        if current_animal == "wolf":
            sheep_in_danger = index
            print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")

'''
animal = list(input().split(", "))

if animal[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    if "wolf" in animal:
        animal.reverse()
        for index, value in enumerate(animal):
            if value == "wolf":
                print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
    else:
        pass

'''

#####   Task Description   ##### 3. Wolf in Sheep's Clothing
# Wolves have been reintroduced to Great Britain. 
# You are a sheep farmer and are now plagued by wolves who pretend to be sheep. 
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. 
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". 
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" 
# where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
# Input
# The input will be a single string containing the animals separated by a comma and a single space ", "
