# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
import string
from anagram_checker import AnagramChecker

checker = AnagramChecker()

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
def menu():
    while True:
        print('==== MENU ====')
        print('1) Input a word')
        print('2) Exit')
        user_choice = input('Choose 1 or 2: ').strip()

        if user_choice == '2':
            print('Exit')
            exit()
    
        elif user_choice == '1':
            user_word = input('Pleace input a word: ')
            
        
            if len(user_word.split()) != 1:
                    print("You should choose only ONE word")
                    continue

            if not all(ch in string.ascii_letters for ch in user_word):
                print("This is not a word. Letters A–Z only. Try again")
                continue

            return user_word.upper()
    
        else:
            print(f'There is no such option: "{user_choice}"')
            continue
            
        

while True:
    word = menu()
    if word is None:
        break

    print(f'\nYOUR WORD : "{word}"')
    if checker.is_valid_word(word):
        print("this is a valid English word.")
        anags = checker.get_anagrams(word)
        if anags:
            print("Anagrams for your word:", ", ".join(sorted(anags)))
        else:
            print("No anagrams found.")
    else:
        print("this is NOT a valid English word.")

          



    

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.
