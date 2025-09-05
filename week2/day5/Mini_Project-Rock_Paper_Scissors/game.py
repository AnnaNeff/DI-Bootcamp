import random

class Game():
    def __init__(self, user_item = None, comp_item = None):
        self.user_item = user_item
        self.comp_item = comp_item
    
    def get_user_item(self):
        print("\nLet's Start!")
    
        while True:
            print("rock - 1\npaper - 2\nscissors - 3")
            user_choice = input("Your choice: ")
            if  user_choice == "1":
                self.user_item = "rock"
            elif user_choice == "2":
                self.user_item = "paper"
            elif user_choice == "3":
                self.user_item = "scissors"
            else:
                print("Incorrect choice.\nChoose 1, 2 or 3")
                continue
            return self.user_item
    
    def get_computer_item(self):
        item_list = ["rock", "paper", "scissors"]
        self.comp_item = random.choice(item_list)
        return self.comp_item
    
    def get_game_result(self, user_item, comp_item):
        item_dict = {"rock": 1, "paper": 2, "scissors": 3}
        user_score = item_dict.get(self.user_item)
        comp_score = item_dict.get(self.comp_item)
        if user_score == 1 and comp_score == 3:
            user_score = 4

        if user_score == 3 and comp_score == 1:
            comp_score = 4
        
        if int(comp_score) > int(user_score):
            return "loss"
        elif int(comp_score) < int(user_score):
            return "win"
        elif comp_item == user_item:
            return "draw"

        
        
    def play(self):
        user_item = self.get_user_item()
        comp_item = self.get_computer_item()
        result = self.get_game_result(user_item, comp_item)

        if result  == "draw":
            print(f"\nThe choice is: your - {user_item}, computer - {comp_item}\nIt's a draw!\n")
        else:
            print(f"\nThe choice is: your - {user_item}, computer - {comp_item}\nYou {result}\n")
        
        return result






    