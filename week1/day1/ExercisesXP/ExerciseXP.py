#Exercise 1
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world


text = "Hello world"
for ן in range (4):
    print(text)


#Exercise 2
# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99 ** 3) * 8
print(result)


#Exercise 3
# Predict the output of the following code snippets:

# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

print(5 < 3)    #False
print(3 == 3)   #True
print(3 == "3") #False
print("3" > 3)  #TypeError
print("Hello" == "hello")   #False


#Exercise 4
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "Apple"
print(f"I have an {computer_brand} computer")


#Exercise 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Anna"
age = 34
shoe_size = 38
info = f"Hi my name is {name}, I\'m {age} year old. Yesterday I've bought sneakers which was smaller then my size, which is {shoe_size}"
print(info)


#Exercise 6
# structions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 10
b = 7
if a > b:
    print("Hello World")


#Exercise 7
# Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Enter the random number: "))
if num % 2 == 0:
    print("This number is even")
else:
     print("This number is odd")


#Exercise 8
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

my_name = "Anna"
user_name = input("What is your name? ")
if user_name == my_name:
    print("I found my mising twin!")
else:
    print("Not so nice to meet u.")


#Exercise 9
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

usrs_height = int(input("Enter your height in centimeters: "))
if usrs_height > 145:
    print("You are are tall enough to ride")
else:
    print("You need to grow some more to ride")
