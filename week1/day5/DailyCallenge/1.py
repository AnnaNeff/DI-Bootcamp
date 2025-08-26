phrase = input("Enter any phrase: ")

def longest_word():
       
    make_list = list(phrase.split())
    max_len = max(len(word) for word in make_list)
    for word in make_list:
        if len(word) == max_len:
            return word

print(longest_word())