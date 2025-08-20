# #BASIC VALUE TYPES

# #STRINGS
# my_name = "Anna"

# #check the lenght
# print(len(my_name))

# #access chars by index (start with 0)
# print(my_name[3])

# #my_name[2] = "J"


# #String functions/ string Methods

# print(my_name.lower())
# print(my_name.upper())
# print(my_name.capitalize())
# print(my_name.title())

# student = "Harry Potter"
# student2 = student.replace("Harry", "Giny")
# print(student2)

# price = "15$"

# clean_price = price.strip("$")
# print(clean_price)


# description = "strings are..."

# print(description.upper())     #make it all uper case
# print(description.replace("are", "is"))    #replace the word "are" to "is"
# print(description.strip("are..."))   # print just the word "strings"
# #or
# print(description[0:7])
# print(description[:6])

# #NUMBERS

# #Integers
# age_int = 34
# age1_int = age_int + 1
# print(age1_int)
# print(5 +(-1))
# print(int(10/2))
# print(10 % 3)

# #Float
# print(3.5 + 3)
# division = 10 / 3
# print(round(division, 2))

# #Type casting

# # #age = int(input("How old are you?"))
# # #print(type(age_int))

# # #print(age + 10)

# # #height = float(input("How old are you?"))

# # age = str(age)
# # print(type(age))

# #BOLEANS (True and False)

# print(5 > 7)
# print("5" == 5)
# print(-1 != 1)

#Adding types

# my_string = "Hello World"
# pyt = "Python is Fun"

# print(my_string + pyt)
# print( my_string * 5)

# print("Hello, aren\'t u happy?")

# day = "Wednesday"
# user_name = input("What\'s your name? ")
# print("Welcoe, <user_name>!")
# print("Welcom, ' + user_name + '!")
# print(f"Welcome, {user_name} today is {day}")

# first_name = "Anna"
# last_name = "Nefedova"
# print (f"Your name is {first_name} {last_name}")
# print (first_name , last_name)

#CONDITIONALS

#SYNTAX
#if (condition)
#(indentend block) <action>

# if 5 > 7:
#     print("Hello there")
# else:
#     print("bebebe")


# user_num = int(input("Guess a number"))
# secret_num = 18
# if user_num == secret_num:
#     print("Congrats! U won!")

# elif user_num == 7:
#     print("It is my luccy number")

# elif user_num < 1:
#     print("Don\'t enter numbers less then 1")

# else:
#     print("try anain")


# user_name = input("Print your name ")
# if len(user_name) <= 5:
#     print(('You have a short name :)'))
# else:
#     print("Your name is looooong")


# my_hobbies = "sport, code, food, icecreams, netflix"
# if "code" or "ff" in my_hobbies:
#     print("Hello world let\'s eat")

number = int(input("Enter number between 1 and 100 "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0: 
    print("Buzz")

else: print("LOOOSEEEER")
