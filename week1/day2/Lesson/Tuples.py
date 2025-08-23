# #TUPLES: immutable and ordered

# numbers = (10, 20, 30, 40, 50)
# number2 = tuple(numbers)
# print(number2)

# # number2[1] = 200 #error because tuple are immutable

# print(number2[1]) #ok

# #methods
# print(numbers.count(20))
# print(numbers.index(20))

# #concatinate tuples
# fruits = ("apple", "mango", "kiwi", "lime")
# vegs = ("tomato", "potato", "lettuce")
# Fruits_vegs = fruits + vegs
# print(Fruits_vegs)

# numbers3 = (1, 2, 3, 4)
# print(1)
# print(2)
# print(3)
# print(4)


# #SETS  = unordered sequence not dublecated elements

# my_set = {1, 4, 8, 9}
# my_set2 = set(my_set)
# print(my_set, my_set2)

# my_set.add(55)
# print(my_set)

# user_name = ["July", "Ann", "John", "bob", "mark", "John"]
# set_user_name = set(user_name)
# clean_user_name = list(set_user_name)
# print(clean_user_name)

# names = {"Juliana", "Israel", "Diana"}
# contries = {"USA", "Brasil", "Israel"}
# print(names.intersection(contries))
# print(names.difference(contries))
# print(contries.difference(names))


my_colors = {"black", "pink", "brown", "orange"}
my_colors.add("violet")
print(my_colors)

my_colors2 = {"black", "pink", "brown", "green", "violet"}
print(my_colors.intersection(my_colors2))
my_colors.clear()
print(my_colors)