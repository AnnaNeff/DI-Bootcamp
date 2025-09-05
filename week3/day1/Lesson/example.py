class Car:
    cars_created = 0
    def __init__(self, make , model):
        
        self.make = make
        self.model = model
        Car.cars_created += 1

c = Car("Ford", "F150")

print(c.model)
print(c.make)

mycar = Car("Toyota", "Auris")
print(Car.cars_created)
print(Car.cars_created)
print(mycar.cars_created)

        