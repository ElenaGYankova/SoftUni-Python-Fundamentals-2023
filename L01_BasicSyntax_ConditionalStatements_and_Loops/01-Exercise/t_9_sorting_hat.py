while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")


'''
command = input()

hats_are_sorted = True
while command != "Welcome!":
    current_name = command
    current_house = ""
    if current_name == "Voldemort":
        hats_are_sorted = False
        print("You must not speak of that name!")
        break
    else:
        if len(current_name) < 5:
            print(f"{current_name} goes to Gryffindor.")
        elif len(current_name) == 5:
            print(f"{current_name} goes to Slytherin.")
        elif len(current_name) == 6:
            print(f"{current_name} goes to Ravenclaw.")
        else:
            print(f"{current_name} goes to Hufflepuff.")
    command = input()
if hats_are_sorted:
    print("Welcome to Hogwarts.")
'''

#####   Task Description   ##### 9. Sorting Hat
# Help out the sorting hat to sort the new students in the houses of Hogwarts. 
# You will be receiving names until the command "Welcome!". 
# The length of each name determines in which house the student is going:
# • If the name is less than 5 chars, the student is going into Gryffindor
#     o Print "{name} goes to Gryffindor."
# • If the name is exactly 5 chars, the student is going into Slytherin
#     o Print "{name} goes to Slytherin."
# • If the name is exactly 6 chars, the student is going into Ravenclaw
#     o Print "{name} goes to Ravenclaw."
# • If the name is more than 6 chars, the student is going into Hufflepuff
#     o Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", 
# print "You must not speak of that name!" and end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."
