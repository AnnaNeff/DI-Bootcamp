# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.



# Key Python Topics:

# datetime module
# Time difference calculations


# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

import  datetime

# Step 2: Get the current date and time

current_time =  datetime.datetime.now()

# Step 3: Create a datetime object for January 1st of the next year

next_year = current_time.year + 1
January1st_next = datetime.datetime(next_year, 1, 1)


# Step 4: Calculate the time difference

difference = January1st_next.__sub__(current_time)

# Step 5: Display the time difference

print(difference)