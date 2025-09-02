# 🌟 Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a specified length from a word list.



# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation


# Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.


# Step 1: Create the get_words_from_file function

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.

import random

file_path = "/Users/annanefedova/Desktop/Учеба /Developers Institute/DI-Bootcamp/week2/day4/Exercises2-4/words.txt"
def get_words_from_file(file_path):

    with open(file_path, 'r', encoding = 'utf-8') as f:    
        return (f.read().split())

# Step 2: Create the get_random_sentence function

# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.

def get_random_sentence(words_number):
    words = get_words_from_file(file_path)
    result = []
    for _ in range(words_number):
        result.append(random.choice(words))
    return " ".join(result).lower()
        
# Step 3: Create the main function

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.
# 

def main():

    print("This program generates a random sentence using random words.")
    user_choice = input("Choose number of words (2-20): ")

    try:
        length = int(user_choice)
    except ValueError:
        print("Error: please enter a valid INTEGER.")
        return

    if 2 <= length <= 20:
        print(get_random_sentence(length))
    else:
        print("Error: number must be between 2 and 20.")
  


main()


# 🌟 Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.



# Key Python Topics:

# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())


# Instructions:

# Using the follow code:

import json
import os

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

dir_path = os.path.dirname(os.path.realpath(__file__))
# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.


# Step 1: Load the JSON string

# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.

data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key

# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add the “birth_date” key

# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.

data["company"]["employee"]["birth_date"] = "1991-04-13"

# Step 4: Save the JSON to a file

# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.

with open(f'{dir_path}/sample.json', "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)


