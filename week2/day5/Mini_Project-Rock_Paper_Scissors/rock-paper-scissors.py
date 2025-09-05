from game import Game

def get_user_menu_choice():
    print("GAME MENU:")
    while True:
        go_to = input(f'For "Play a new game” - enter "1"\nFor “Show scores” - enter "2"\nFor “Quit" - enter "3"\nYour choice: ')
        if go_to == "1"  or go_to == "2" or go_to == "3":
            return go_to
        else:
            print("Incorect input")
            continue

results = {"win": 0, "loss": 0, "draw": 0}

def print_results(results):
    print(f'\nWins: {results["win"]}, Losses: {results["loss"]}, Draws: {results["draw"]}\n')
   

def main():
    while True:
        user_choice = get_user_menu_choice()

        if user_choice == "1":
            new_game = Game(None, None)
            result = new_game.play() 
            results[result] += 1

        elif user_choice == "2":
            print_results(results)

        elif user_choice == "3":
            print_results(results)
            print("Thank you for playing!\nSee you soon")
            break
        else:
            print("Incorect input/n")
            continue

if __name__ == "__main__":
    main()
