age = int(input())

this = ''
if age <= 14:
    this = "toddy"
elif age <= 18:
    this = "coke"
elif age <= 21:
    this = "beer"
else:
    this = "whisky"

print(f"drink {this}")

#####   Task Description   ##### 2. Drink Something
# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. 
# Create a program that receives a person's age and prints what he/she drinks.
# Rules:
# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!
