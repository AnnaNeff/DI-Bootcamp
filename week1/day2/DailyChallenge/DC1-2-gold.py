# Daily challenge GOLD : Happy birthday
# Last Updated: March 10th, 2025

# What You will learn :
# Python Basics
# Conditionals


# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !

cake = [
    "___iiiii___",
    "|:H:a:p:p:y:|",
    "__|___________|__",
    "|^^^^^^^^^^^^^^^^^|",
    "|:B:i:r:t:h:d:a:y:|",
     "|                 |",
     " ~~~~~~~~~~~~~~~~~~~"
]

age = int(input("Enter your age"))
cake[0] = str("i" * (age % 10))

max_len = max(len(r) for r in cake)

final_cake = [r.ljust(max_len) for r in cake]
print("\n".join(final_cake))