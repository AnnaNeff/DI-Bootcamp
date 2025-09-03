import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker():
    def __init__(self): # should load the word list file (text file) into a variable, so that it can be searched later on in the code.
        
        with open(f'{dir_path}/sowpods.txt', "r", encoding="utf-8") as f:
            self.sowpods = f.read().split()

         
    def is_valid_word(self, word): # should check if the given word (ie. the word of the user) is a valid word.
       if word.upper() in self.sowpods:
           return True
       else:
           return False

    def get_anagrams(self, word): # should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
        word = word.upper()
        return [w for w in self.sowpods if sorted(w) == sorted(word) and w != word] 
    
    @staticmethod
    def is_anagram(self, word1, word2 = None):   # Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
        if sorted(word1) == sorted(word2) and word1 != word2:
            return True
        else:
            return False

# Note: None of the methods in the class should print anything.
