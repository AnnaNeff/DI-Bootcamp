# 1. Ask for User Input:

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:

# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:

# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:

# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.

# 5. Bonus: Jumble the String (Optional)

# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.

while True:
    string = input("Print the string exactly 10 characters long ")
    String_len = False
    if len(string) > 10:
        print("String too long.")
        
    elif len(string) < 10:
        print("String not long enough.")
        
    else:
        print("Perfect string")
        String_len = True
        break

if String_len == True:
     
    print(f"The firas character in your strin is {string[0]}")
    print(f"The last haracter in your strin is {string[-1]}")
    for i in range(1, len(string)):
        print(string[:i])

    import random
    simbols = list(string)
    random.shuffle(simbols)
    shuffeled_string = "".join(simbols)
    print(f"Shuffeled: {shuffeled_string}")