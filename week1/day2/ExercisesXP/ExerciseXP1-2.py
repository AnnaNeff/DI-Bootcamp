
# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)

# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {4, 7, 13, 8, 9, 21, 25, 34, 57, 79, 98} 
print("My fav numbers:", my_fav_numbers)

my_fav_numbers.update([101, 122])
print("After adding:", my_fav_numbers)

my_fav_numbers.remove(122)
print("After removing:", my_fav_numbers)

friend_fav_numbers = {4, 11, 13, 15, 9, 22, 25, 35, 57, 55, 98}
print("Friend's fav numbers:", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) 
print("Our fav numbers:", our_fav_numbers)



# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)

# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

my_tuple = (4, 7, 13, 8, 9, 21, 25, 34, 57, 79, 98 )
my_set = set(my_tuple)
my_set.update({133, 122})
my_tuple = tuple(my_set)
print(my_tuple)



# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear

# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana") #['Apples', 'Oranges', 'Blueberries']
basket.remove("Blueberries")    #['Apples', 'Oranges']
basket.insert(0, "Kiwi")    #['Kiwi', 'Apples', 'Oranges']
basket.insert(0, "Apples")  #['Apples', 'Kiwi', 'Apples', 'Oranges']

print(basket.count("Apples"))   #2
basket.clear()
print(basket)



# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation

# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

numbers = list(n/2 for n in range(3,21))

for idx in range(len(numbers)):
    if numbers[idx] - int(numbers[idx]) == 0:
        numbers[idx] = int(numbers[idx]) 
    else:
        numbers[idx] = numbers[idx] 

print(numbers)



# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

my_list = list(n for n in range(1, 21))
print(my_list)

my_list_even = list(n for n in my_list if n % 2 == 0)
print(my_list_even)



# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

my_name = "Anna"
while True:
    user_name = input("Enter your name: ")
    if user_name == my_name:
        break


# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

users_fav_fruits = list(input("Enter your favorite fruits (You can input several fruits, separated by spaces: ").split())
users_fruit = input("Enter a name of any fruit: ")
if users_fruit in users_fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")



# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

pizza_toppings = list()
while True:
    topping = input("Please enter pizza toppings one by one: ")
    if topping == "quit":
        toppings_str = ", ".join(pizza_toppings)
        print(f"Your order: one pizza winh {toppings_str}. Final price: {10 + 2.50 * int(len(pizza_toppings))}$")
        break
    else: pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")



# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_prise = 0
while True:
    age_input = input("Enter age of family member (or type 'quit' to finish): ")
    if age_input.lower() == "quit":
        break
          
    age = int(age_input)   
    if age <= 3:
        tiket_prise = 0
    elif 3 < age <= 12:
        tiket_prise = 10
    else:
        tiket_prise = 15
    
    total_prise += tiket_prise

if age_input.lower() == "quit":
    print(f"The total ticket cost is: ${total_prise}")


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

attendees = []
while True:
    age_input = input("Enter your afe (or type 'quit' to finish): ")
    if age_input.lower() == "quit":
        break
       
    age = int(age_input)   
    if 16 <= age <= 21:
        attendees.append(age)
    else:
        print(f"Sorry. If your age is {age}, you are not allowed for this movie")
    
if age_input.lower() == "quit":
    print(f"The total ticket cost is: ${len(attendees) * 15} for {len(attendees)} persons. ")



# 🌟 Exercise 10: Sandwich Orders
# Key Python Topics:

# Lists
# Loops (while)


# Instructions:

# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
     print(f"I made your {sandwich} sandwich.")
