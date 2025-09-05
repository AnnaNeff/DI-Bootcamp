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
import os

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

    def word_frequency(self, word: str):
        words = self.text.split()
        count = sum(1 for w in words if w.lower() == word.lower())
        return count if count > 0 else None


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
            word_freq[word.lower()] = word_freq.get(word, 0) + 1

        most_common = max(word_freq, key=word_freq.get)
        
        return most_common
    

# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.
    def unique_words(self):
        table = str.maketrans("", "", string.punctuation)
        cleaned_text = self.text.translate(table).lower()

        words = cleaned_text.split()

        return sorted(set(words))

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = cls(f.read())
            return text


# Bonus: Text Modification

# Step 6: Create the TextModification Class
class TextModification(Text):
    def __init__(self, text: str):
        super().__init__(text)
    

            
# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.
    def remove_punctuation(self, in_place: bool = True):
        table = str.maketrans("", "", string.punctuation)
        cleaned = self.text.translate(table)
        if in_place:
            self.text = cleaned
            return self.text
        return cleaned

    def remove_stop_words(self, stop_words: set[str] = None, in_place: bool = True):
        if stop_words is None:
            stop_words = {"a", "an", "the", "is", "are", "am", "to", "and", "of", "in"}
        tokens = [t for t in re.split(r"\W+", self.text.lower()) if t]
        kept = [t for t in tokens if t not in stop_words]
        result = " ".join(kept)
        if in_place:
            self.text = result
            return self.text
        return result

 
    def remove_special_characters(self, in_place: bool = True):
        cleaned = re.sub(r"[^\w\s]", "", self.text)
        if in_place:
            self.text = cleaned
            return self.text
        return cleaned

if __name__ == "__main__":
 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = "Alise.txt"
    file_path = f"{dir_path}/{file_name}"

    t1 = Text("Hello, hello! This is a test. Hello?")
    print("word_frequency('This'):", t1.word_frequency("This"))
    print("most common word:", t1.most_common_word())
    print("unique words:", t1.unique_words())

    if os.path.exists(file_path):
        t2 = Text.from_file(file_path)
        print("word_frequency('Alice') in file:", t2.word_frequency("Alice"))

    tm = TextModification("Hello, hello! This is a test. Hello?")
    tm.remove_punctuation()
    tm.remove_stop_words()
    tm.remove_special_characters()
    print("modified text:", tm.text)
    print("most common word:", t2.most_common_word())
    

