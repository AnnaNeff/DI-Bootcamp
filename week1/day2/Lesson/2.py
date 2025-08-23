string1 = input("Etter a string: ")
list1 = list(string1)
list2 = []
prev_letter = None
for letter in list1:
    if letter != prev_letter:
        list2.append(letter)
        prev_letter = letter   
        
string = "".join(list2)
print(string)
