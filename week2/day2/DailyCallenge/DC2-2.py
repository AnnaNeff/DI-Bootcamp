# Daily Challenge : Pagination

# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Classes and Objects
# Method chaining
# List slicing and indexing
# Error handling
# Type conversion


# Key Python Topics:

# Classes and Objects
# Constructors and instance attributes
# List slicing and indexing
# Method chaining (return self)
# Type casting (int())
# Conditional logic
# Custom exceptions


# Instructions: Pagination System

# 📄 What is Pagination?

# In web development, pagination helps break large lists into smaller, manageable chunks (pages), making it easier to navigate content like search results, product listings, or articles.

# Here’s a visual example:

# Page 1      Page 2      Page 3
# [a, b, c]   [d, e, f]   [g, h, i]


# Goal:

# Create a Pagination class that simulates a basic pagination system.



# Step 1: Create the Pagination Class

# Define a class called Pagination to represent paginated content.
# It should optionally accept a list of items and a page size when initialized.
import math

class Pagination:
    def __init__(self, items = None, page_size = 10,):
        self.items = [] if items is None else list(items)
        self.size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / int(page_size))
        


# Step 2: Implement the __init__ Method

# Accept two optional parameters:
# items (default None): a list of items
# page_size (default 10): number of items per page

# Behavior:

# If items is None, initialize it as an empty list.
# Save page_size and set current_idx (current page index) to 0.
# Calculate total number of pages using math.ceil.


# Step 3: Implement the get_visible_items() Method

# This method returns the list of items visible on the current page.
# Use slicing based on the current_idx and page_size.

    def get_visible_items(self):
        
        start = self.current_idx * self.size
        end = start + self.size
        visible_items = self.items[start:end]
        return visible_items


# Step 4: Implement Navigation Methods

# These methods should help navigate through pages:

    def go_to_page(self, page_num):
# → Goes to the specified page number (1-based indexing).
# → If page_num is out of range, raise a ValueError.
        if page_num <= self.total_pages: 
            self.current_idx = page_num - 1
            return self
        else:
            raise ValueError("Page out of range")


    def first_page(self):
        self.current_idx = 0
        return self
# → Navigates to the first page.


    def last_page(self):
         self.current_idx = self.total_pages -1
         return self
# → Navigates to the last page.

    def next_page(self):
         self.current_idx = self.current_idx + 1
         
         return self
# → Moves one page forward (if not already on the last page).

    def previous_page(self):
         self.current_idx = self.current_idx - 1
         return self
# → Moves one page backward (if not already on the first page).

# 📝 Note:

# Pages are indexed internally from 0, but user input is expected to start at 1.
# All navigation methods (except go_to_page) should return self to allow method chaining.


# Step 5: Add a Custom __str__() Method
    def __str__(self):
        chs = []
        for ch in self.get_visible_items():
            chs.append(ch)
        return "\n".join(chs)
        

# This magic method should return a string displaying the items on the current page, each on a new line.
# Example:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# Output:
# a
# b
# c
# d


# Step 6: Test Your Code

# Use the following test cases:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(7)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(9)
# Raises ValueError


