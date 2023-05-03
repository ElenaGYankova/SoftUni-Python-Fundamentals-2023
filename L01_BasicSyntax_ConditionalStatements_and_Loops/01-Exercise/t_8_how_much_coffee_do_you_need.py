command = ''

coffees_needed = 0
while command.lower() != "end":
    command = input()
    if command.lower() == 'coding' or command.lower() == 'dog' \
            or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            coffees_needed += 1
        else: #elif command.isupper():
            coffees_needed += 2
if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)

'''
command = input()

event_list_lowercase = ["coding", "dog", "cat", "movie"]
event_list_uppercase = ["CODING", "DOG", "CAT", "MOVIE"]

number_of_coffees = 0
while command != "END":
    event = command
    if event in event_list_lowercase:
        number_of_coffees += 1
    elif event in event_list_uppercase:
        number_of_coffees += 2
    command = input()
if number_of_coffees <= 5:
    print(number_of_coffees)
else:
    print("You need extra sleep")
'''

#####   Task Description   ##### 8. How Much Coffee Do You Need?
# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake. 
# Until you receive the command "END", you need to read commands on different lines. 
# According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
# The list of events can contain the following:
# • You have homework to do ("coding").
# • You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# • You watch a movie ("movie").
# • If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# • If it is lowercase, you need 1 coffee by an event.
# • If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. 
# If the count has exceeded 5, just print "You need extra sleep".
