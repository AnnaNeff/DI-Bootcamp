
class Farm:
    def __init__(self, farm_name, animals = {}):
        self.name = farm_name
        self.animals = animals
    
    def add_animal(self, animal_type, count = 1):
        animals = {}
        if animal_type in animals:
            animals[animal_type] = int(count) + 1
        else:
            animals[animal_type] = count

farm_name = "Farm"
Farm.add_animal("Cow", 1)

name = "Mcdonald"
name1 = name + "'s"

print(name1)