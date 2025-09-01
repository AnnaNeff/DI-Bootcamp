# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.



# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.



# Key Python Topics:

# String concatenation


# Step 1: Import the string and random modules

# Import the string and random modules.

import string
import random

# Step 2: Create a string of all letters

# Read about the strings methods HERE to find the best methods for this step
letters = string.ascii_letters  

# Step 3: Generate a random string

# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.
result = ""
for i in range(5):
    result += random.choice(letters) 
print(result)
