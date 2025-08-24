# Example 1
sample_dict1 = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict1["class"]["student"]["marks"]["history"])

# x = sample_dict.get("history") #dom't work with mixed dects, only we can get "class"
# print(x)


# Example 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
   if key in sample_dict:
      del sample_dict[key]

print(sample_dict)


# Example 3
grades = {
   "mike": 70,
   "Sarah": 85,
   "Tom": 90,
   "Anna": 65,
   "Miriam": 50
}

for name, score in grades.items():
   if score >= 70:
      print(f"{name} passed the exam")