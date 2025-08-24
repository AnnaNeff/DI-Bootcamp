users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

users_dict1 = dict({})
for user in users:
    users_dict1[user] = users.index(user)

print(users_dict1)


users_dict2 = dict({})
for user in users:
    users_dict2[users.index(user)] = user

print(users_dict2)


users_sorted = sorted(users)
users_dict3 = dict({})
for user in users_sorted:
    users_dict3[user] = users_sorted.index(user)
print(users_dict3)
