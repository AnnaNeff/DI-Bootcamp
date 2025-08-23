string1 = input("Etter a string: ")
list1 = list(string1)
list2 = []
ind = list1.index()
for letter in list1:
    for i in range(0,len(list1) +1):
        if letter[i] == letter[i - 1]:
            list1.remove(letter)
        else:
            list2.append(letter) 
        
        string = str(list2)
        print(string)
