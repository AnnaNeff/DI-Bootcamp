#🌟 Exercise 1: Cats
# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.

cat1 = Cat("Fluffy", 2)
cat2 = Cat("Kot", 8)
cat3 = Cat("Matilda", 4)

# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    for cat in [cat2, cat3]:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

print(f"“The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


#🌟 Exercise 2 : Dogs

# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “ goes woof!”.
# Create a jump() method that prints “ jumps cm high!”, where x is height * 2.

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        return f'{self.name} goes woof!'

    def jump(self):
        jump_height = self.height * 2
        return f'{self.name} jumps {jump_height} cm high!'

# Step 2: Create Dog Objects

# Create davids_dog and sarahs_dog objects with their respective names and heights.

davids_dog = Dog("Bro", 20)
sarahs_dog = Dog("Chichi", 45)

# Step 3: Print Dog Details and Call Methods

# Print the name and height of each dog.

print(f"David's dog {davids_dog.name} is {davids_dog.height} sm height.")
print(f"Sarah's dog {sarahs_dog.name} is {sarahs_dog.height} sm height.")

# Call the bark() and jump() methods for each dog.
dogs = [davids_dog, sarahs_dog]
for dog in dogs:
    print(dog.bark())
    print(dog.jump())


# Goal: Create a Song class to represent song lyrics and print them.

# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists


#🌟 Exercise 3 : Who’s the song producer?

# Instructions:

# Create a Song class with a method to print song lyrics line by line.

class Song:
    def __init__(self, song_name, lyrics):
        self.name = song_name
        self.lyrics = list(lyrics)

    def sing_me_a_song(self):
        for str in self.lyrics:
            print(str)
            

# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


# Example:

stairway = Song("stairway",["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
# Goal:

# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.



# Key Python Topics:

# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation


# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

class Zoo:
    def __init__(self, zoo_name, animals =[]):
        self.name = zoo_name
        self.animals = animals

# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):

# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            return self.animals
        
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
    def get_animals(self):
        for animal in self.animals:
            print(animal)

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            
        
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.

    def sort_animals(self):
        groups = {}
        for animal in sorted(self.animals):
            group_key = animal[0]
            if group_key in groups:
                groups[group_key].append(animal)
            else:
                groups[group_key] = [animal]
        
        return groups
    
# Example output:

# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
# 7. Add a method get_groups():
    
    def get_groups(self):
        groups = self.sort_animals()
        for key, value in groups.items():
            print(f'{key.upper()}: {value}')

# This method prints the grouped animals as created by sort_animals().
# Example output:

# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...


# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.

brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.


# Example (No Internal Logic Provided)
# class Zoo:
#     def __init__(self, zoo_name):
#         pass

#     def add_animal(self, new_animal):
#         pass

#     def get_animals(self):
#         pass

#     def sell_animal(self, animal_sold):
#         pass

#     def sort_animals(self):
#         pass

#     def get_groups(self):
#         pass

# # Step 2: Create a Zoo instance
# brooklyn_safari = Zoo("Brooklyn Safari")

# # Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.add_animal("Bear")
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
