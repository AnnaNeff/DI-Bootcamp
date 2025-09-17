import random

def number_guessing_game_2():
    number_to_guess =  random.randint(1, 100)
    max_attempts = 7
    final_msg = f"You didn't guess... The secret number was {number_to_guess}."

    for attempt in range(max_attempts):
       guess = int(input("Guess the number between 1 and 100: "))
       if guess == number_to_guess:
          final_msg = "Congrats! U guessed"
          break
       elif guess > number_to_guess:
          print("Too high!")
       else:
          print("Tu low!")
    print(final_msg)

number_guessing_game_2()