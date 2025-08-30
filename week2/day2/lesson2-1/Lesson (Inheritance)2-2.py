#OOP - Inheritance

class Animal: #the parent class

    def __init__(self, name, family, legs = None):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        print(f'{self.name} is sleeping (parent class)')

    
class Dog(Animal): #the child class

    def __init__(self, name, family, legs, age, trained):
        super().__init__(name, family, legs)
        self.age = age
        self.trained = trained
    
    def sleep(self):
        print(f'{self.name} is sleeping (child class)')

    def fetch_ball(self):
        print(f'{self.name} is running for the ball')

class Cat(Animal):
    
    def sleep(self):
        base_mg = super().sleep
        print

dog1 = Dog('Rex', 'Canine', 10, True)
print(dog1.legs)
dog1.sleep()
dog1.fetch_ball()

horse1 = Animal('Spirit', 'Equidae', 4)
# horse1.fetch_ball()

#create the method sleep() on the child class, change the "(parent class)" to "child class"
# call the method on the dog1 object