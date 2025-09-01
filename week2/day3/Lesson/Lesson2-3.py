# Decorators are python built -in functions that "apply" to uor function within the class i. e methods
from datetime import datetime, date

class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
        self._email = None  #Protected attribute - the underscore here is a convension in python. This ractise is calling Incapsulations

    @staticmethod   #Method don't need self
    def format_name(name):
        return name.capitalize()
    
    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str, '%d-%m-%Y').date()
    
    
    @staticmethod
    def from_age(cls, first_name, last_name, age:int):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f'1-01-{birth_year}'
        return cls(first_name, last_name, birth_date)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    @property
    def email(self):
        initial = self.first_name[0].lower()
        email = f'{initial}.{self.last_name.lower()}@gmail.com'
        return email

    ######## DUNDER METHOD (It's better to use signs from using insructions)
    def __str__(self):
        return f'Hello this is {self.first_name} {self.last_name}' #we dont need to call it, it's automaticly when we print
    
    def __repr__(self):
        return f'{self.__dict}'
    
    def __eq__(self, other):
        return self.last_name == other.last_name
    
    def __lt__(self, other):
        return self.age > other.age
    
    def __add__(self)


p1 = Person("john", "snow da silva", "21-08-1990")
# print(p1.birth_date)
# print(p1.first_name)
# print(p1.birth_date)
# print(p1.age)
# print(p1.email)

# #How to use a class method when creating  the object

p2 = Person.from_age('aria', 'stark', 18)
p3 = Person.from_age('Sansa', 'stark', 21)
# print(p2.birth_date)

print(p2 == p3)