animals = ["jiraf", "tiger", "elephant"]
def sort_animals(animals):
        groups = {}
        for animal in animals:
            for animal[0] in groups.keys():
                if animal[0] in groups.keys():
                    groups[animal[0]].append(animal)
                else:
                    groups[animal[0]] = [animal]
        return groups
print(sort_animals(animals))
