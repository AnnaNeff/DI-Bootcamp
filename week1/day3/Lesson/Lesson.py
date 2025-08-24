#DICTIONARIES: data structure but moe complex. It allows us to "LABEL" the data inside the structure

user_info = ["Anna Neff", "anna@gmail.com", 539534003, ("Ramat Gan", "St. Peterburg")]

print(user_info[1])

#Syntax: {key: value, key: value}

user_info = {"Full_name" : "Anna Neff",
            "email": "anna@gmail.com",
            "score": "0539534003",
            "addresses": ("Ramat Gan", "St. Peterburg")
            }

#ACCESSING DATA

print(user_info["email"])
print(user_info["addresses"])
print(user_info["addresses"][1])

#ADD KEY:VALUE

user_info["family"] = ["Sofia", "Liza"]
print(user_info)

user_info.update({"hobbies": ["yoga", "playstation"]}) #??????????????

#changing data inside the dict

user_info["family"].append(["Mom", "Dad"])
user_info["family"][1] = "Elizabeth"

saved_value = user_info["score"]

del user_info["score"]  #How to delite key:value pair

user_info["balance"] = saved_value

print(user_info)

#METHODS

# print(user_info["email"].upper()) #??????????????
# user_info["balance"] += 10000

# print(user_info)




student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 14,
    'address' : 'Privet Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'houses': {'main': 'Griffyndor', 'second': 'Slytherin'},
    'best_friends': ('Ron Weasley', 'Hermione Granger')
}

for key in student_info.keys():
    print(key)

for value in student_info.values():
    print(value)

for key, value in student_info.items():
    print(key, value )



#Other very useful built - in methodes

#enumerate -> Allowes us to access the index and the element of sequence

studients = ["Harry", "Ron", "Hermione", "Draco", "Luna"]

for name in studients:
    print(f'Welcome {name}')

for name in studients:
    studients[0] = f"Welcome {name}"     #????????????

print(studients)


#ZIP
grades = [100, 85, 90, 60, 75]
studients = ["Harry", "Ron", "Hermione", "Draco", "Luna", "Nevil"]
student_grates = dict(zip(studients, grades))
print(student_grates)


#list comprehension

numbers = list(range(1,11))
squared_numbers = []
for num in numbers:
    squared = num ** 2
    squared_numbers.append(squared)
print(squared_numbers)

squared_numbers = [num ** 2 for num in numbers if num %2 ==0]
print(squared_numbers)