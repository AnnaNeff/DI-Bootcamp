# Daily challenge : Text Analysis
# Last Updated: August 21st, 2025

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques


# Key Python Topics:

# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)

import string
import re

# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.



# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g., self.text).

class Text:
    def __init__(self, text:str):
        self.text = text
        

# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

def word_frequency(self, word):
    
    text_list = [self.text.split()]
    if word in text_list:
        counter =  text_list.count(word)
    else:
        counter = None
        return counter



# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

def most_common_word(self):
     word_freq = {}
     text_list = self.text.split()
     
     for word in text_list:
        word_freq[word] = word_freq.get(word, 0) + 1

     most_common = max(word_freq, key=word_freq.get)
     
     return most_common
    

# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.
def unique_words(self):

    text_list = self.text.split()
    unic_word = set(text_list)
    unic_text_list = list(unic_word)
    return unic_text_list

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

def rom_file(self, file_path):
    file_path = 

# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.


# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.


# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.