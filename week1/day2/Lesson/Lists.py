#list methods
fruits = ["apple", "mango", "kiwi", "lime"]

fruits.append("banana") #adding on the end of the list

print(len(fruits))
print(fruits)

fruits.insert(1, "watermelon") #ading element on the certien position
print(fruits)

fruits.remove("mango") #delete just first appereance
print(fruits)

fruits.pop() #with no argumetn deletes the last position
print(fruits)

fruits.pop(2) #argument - the index element
print(fruits)


list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:

    list1.remove(20)
    list1.insert(3, 200)
    print(list1)