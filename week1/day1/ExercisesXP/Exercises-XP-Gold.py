# Exercise 1 : Hello World-I love Python
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

text1 = "Hello world"
text2 = "I love python"
for ן in range (4):
    print(text1)
for ן in range (4):
    print(text2)

# Exercise 2 : What is the Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

while True:
    month = int(input("Write a month (1 to 12): "))
    if month  == 1 or month == 2 or month == 12:
        print("Winter")
    elif month == 3 or month == 4 or month == 5:
        print("Spring")
    elif month == 6 or month == 7 or month == 8:
        print("Summer")
    elif month == 9 or month == 10 or month == 11:
        print("Autumn")
    else:
        print("There are only 12 months...")
