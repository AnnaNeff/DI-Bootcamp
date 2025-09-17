import random

def number_guessing_game():
     number_to_guess = random.randint(1, 100)
     max_attempts = 7
     
     for attempt in range(max_attempts):
         guess = int(input("Guess the number between 1 and 100: "))
         if guess == number_to_guess:
           print("Congrats! U guessed")
           break
         elif guess > number_to_guess:
            print("Too high!")
         else:
            print("Tu low!")
          
         if attempt == max_attempts - 1:
            print(f"You didn't guess... The secret number was {number_to_guess}.")

number_guessing_game()
