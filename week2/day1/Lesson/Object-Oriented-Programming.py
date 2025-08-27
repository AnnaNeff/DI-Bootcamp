#OOP: OBJECT ORIENTED PROGRAMING

#Class = a blueprint of the object, where we will define what are the properties and behaviors of the object

#syntax

class Dog:
    
    #the constructor function
    def __init__(self, breed, nickname, color, age, is_trained = False):
        print(self)
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.age = age
        self.is_trained = is_trained
        if age == None:
            self.dot_years_age = None
        else:    
            self.dot_years_age = age * 7

        

######### Methods = the behavior of the object #########

    def bark(self):
        print(f'{self.nickname } is barking')

    def sit(self):
        if self.is_trained:
            print(f'{self.nickname} is sitting')
        else:
            print(f'{self.nickname} if not trained')

    def rename(self, new_name):
        self.nickname = new_name
        pass
    

#creating an object from the class Dog:
dog1 = Dog('chowchow', 'lion', 'orange', 5)
dog2 = Dog('collie', 'laddy', 'bege and white', 15, True)

#creayinf a specific attrebutes of the object
dog2.is_service_dog = True

print(dog1.color) #dot notation to access the attributes of the object

print(dog1.__dict__)
print(dog2.__dict__)

# self is the internal dictionary that has the properties from the class
# {breed: -----, nickname: -------, color: -------}

#create a new attribute to the Dog class called "is_trained" the value is a boolean and the default is False
#then run the code again. What happens with the objects that were created before this new attribute was added?


######### Methods = the behavior of the object #########

dog3 = Dog("labradore", "Rex", "gold", 7, True)
dog3.bark() #calling the method of the object
Dog.bark(dog3)

dog3.sit()
dog1.sit()
dog3.rename("Bob")
print(dog3.nickname)


#create a method to rename (new_name) a dog. Use the attribute to do so

my_dogs = [dog1, dog2, dog3]
for dog in my_dogs:
    print(dog.bark)

print(dog1)



