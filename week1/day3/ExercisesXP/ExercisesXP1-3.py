# Exercises XP
# Last Updated: April 30th, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Working with dictionaries
# Loops (for loops)
# Conditionals (if, elif, else)
# Creating and accessing nested data structures


# 🌟 Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions

# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.



# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]


# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)



# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for key, value in family.items():
    age = value
    name = key
    if 3 <= age <= 12:
            ticket_price = 10 
    elif age > 12:
            ticket_price = 15 
    else:
            ticket_price = 0
        
    print(f'{name} - {ticket_price}$')
    total_cost += ticket_price


print(f'Total cost: {total_cost} $')

# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = dict({})
total_cost = 0

while True:
    new_guest_name = input('Enter the name of a guest or \"continue": ')
    if new_guest_name != "continue":
        new_guest_age = int(input("Enter guest's age: "))
        family.update({new_guest_name: new_guest_age})
    else:
        break

for key, value in family.items():
    age = value
    name = key
    if 3 <= age <= 12:
            ticket_price = 10 
    elif age > 12:
            ticket_price = 15 
    else:
            ticket_price = 0
        
    print(f'{name} - {ticket_price}$')
    total_cost += ticket_price


print(f'Total cost: {total_cost} $')


# 🌟 Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions

# Create and manipulate a dictionary that contains information about the Zara brand.



# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.
zara_brand = dict({})
zara_brand["name"] = "Zara"
zara_brand["creation_date"] = 1975
zara_brand["creator_name"]= "Amancio Ortega Gaona"
zara_brand["type_of_clothes"] = ["men", "women", "children", "home"]
zara_brand["international_competitors"] = ["Gap", "H&M", "Benetton"]
zara_brand["number_stores"] = 7000

major_color_dict = dict({})
major_color_dict["France"] = ["blue"]
major_color_dict["Spain"] = ["red"]
major_color_dict["US"] = ("pink", "green")

zara_brand["major_color"] = dict(major_color_dict)

zara_brand["number_stores"] = 2 #Change the value of number_stores to 2.
print(f"Zara's clients using {", ".join(zara_brand["type_of_clothes"])} clothes.")  #Print a sentence describing Zara’s clients using the type_of_clothes key.

zara_brand["country_creation"] = ["Spain"]  #Add a new key country_creation with the value Spain.

for keys in zara_brand:
    if "international_competitors" in keys:
        zara_brand["international_competitors"].append("Desigual")   #Check if international_competitors exists and, if so, add “Desigual” to the list.

print(zara_brand)

del zara_brand["creation_date"] #Delete the creation_date key.

print(zara_brand["international_competitors"][-1])    #Print the last item in international_competitors.

print(f"The major colors in the US are {" and ".join(zara_brand["major_color"]["US"])}")    #Print the major colors in the US.

print(len(zara_brand))  #Print the number of keys in the dictionary.

for key in zara_brand.keys():   #Print all keys of the dictionary.
    print(key)


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = dict({})
more_on_zara["creation_date"] = 1975
more_on_zara["number_stores"] = 7000

key_list = []
value_list = []
for key in zara_brand.keys():
    key_list.append(key)
for key in more_on_zara:
    key_list.append(key)

for value in zara_brand.values():
    value_list.append(value)
for value in more_on_zara.values():
    value_list.append(value)

new_zara_info = dict(zip(key_list, value_list))
print(new_zara_info)



# 🌟 Exercise 4: Disney Characters
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting


# Instructions

# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:



# Character List:

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# Expected Results:

# 1. Create a dictionary that maps characters to their indices:

# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# 2. Create a dictionary that maps indices to characters:

# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

users_dict1 = dict({})
for user in users:
    users_dict1[user] = users.index(user)

print(users_dict1)


users_dict2 = dict({})
for user in users:
    users_dict2[users.index(user)] = user

print(users_dict2)


users_sorted = sorted(users)
users_dict3 = dict({})
for user in users_sorted:
    users_dict3[user] = users_sorted.index(user)
print(users_dict3)



