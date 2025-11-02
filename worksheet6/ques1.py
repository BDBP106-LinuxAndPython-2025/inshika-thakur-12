#!/usr/bin/python3

"""1.) Define a class called ’Car’. The class intance should take required arguments as make,
model, year and color. Define default values of ’False’ for the attributes called ’started’,
0 for the attribute ’speed’, and ’200’ as the maximum speed. There should be a total of
7 attributes in the __init__ function."""

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

"""a)Create an instance of the above class called toyota_camry with arguments of car
make as ’Toyota’, model as ’Camry’, year as ’2022’ and color ’Red’. Print the values of
these attributes using the instance you just created."""

toyota_camry = Car('Toyota', 'Camry', 2022, 'Red')
print('The car make is: ',toyota_camry.make)
print('The model is: ',toyota_camry.model)
print('The year is: ',toyota_camry.year)
print('Colour: ',toyota_camry.color)

print(f"=============================================")

"""(b) Create another instance of this class called ’ford mustang’ with make as ”Ford”,
model as ”Mustang”, year 2022 and color ’Black’.Print all the 7 attributes for this in-
stance."""

fordMustang = Car('Ford', 'Mustang', 2022, 'Black')
print('Make: ',fordMustang.make)
print('The model is: ',fordMustang.model)
print('The year is: ',fordMustang.year)
print('The colour is: ',fordMustang.color)
print('Started: ',fordMustang.started)
print('Speed: ',fordMustang.speed)
print('Maximum speed: ',fordMustang.max_speed)

print(f'==========================================================================')

"""(c)How can you be sure that the above attributes belong to the instance and not the
class? Try typing print(Car.make). Do you get an error, and if so what error do you
get? How will you fix this error in your main program?"""
#print(Car.make)
"""Yes I got an error typing print(Car.make). The error that I got was AttributeError:
type object 'Car' has no attribute 'make'. Make here is not a class attribute but an instance 
attribute, which means that it belongs to each specific car, not the class car itself.
In order to fix this error we need to change the car to a specific car, eg: toyota_camry"""
print(toyota_camry.make)

print(f'============================================================================')

"""(d)Execute the command print(Car.__dict__). Describe the output. The __dict__
attribute holds a dictionary containing the writable members of the underlying class or
instance. Each key value represents an attribute or method name. When you access a
class member through the class object, Python automatically searches for the member’s
name in the __dict. If the name isn’t there, you get an AttributeError."""

print(Car.__dict__)
#Output: {'__module__': '__main__', '__init__': <function Car.__init__ at 0x7dc808241580>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
"""This prints a dictionary of attributes and methods defined for the class itself (not for
instances). We got to saw keys like __init__ (the constructor function), __module__, and 
others including any class variables"""

print(f'============================================================================')

"""(e)Now define a class attribute called showroom with value NewAge. Also define a func-
tion with decorator @classmethod that changes this value upon user request. Again
print the value of __dict__ attribute, what is the output? Describe the output."""


class Car:
    showroom = 'NewAge'
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    @classmethod
    def change_showroom(cls, new_name):
        cls.showroom = new_name
Car.change_showroom('AutoSpace')
print(Car.showroom)
print(Car.__dict__)

print(f'=======================================================================')

"""(f)Print the value of toyota_camry.__dict__. How is this output different from
Car.__dict__? Explain."""
print(toyota_camry.__dict__)
#output: {'make': 'Toyota', 'model': 'Camry', 'year': 2022, 'color': 'Red', 'started': False, 'speed': 0, 'max_speed': 200}
print(Car.__dict__)
#output: {'__module__': '__main__', 'showroom': 'AutoSpace', '__init__': <function Car.__init__ at 0x72aa1a9ad4e0>, 'change_showroom': <classmethod(<function Car.change_showroom at 0x72aa1a9ad580>)>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
"""The outputs are different from each other as toyota_camry.__dict__ prints only the 
attributes specific to the toyota_camry instance, like make, model, year, etc. It does not 
show methods or class-wide variables like showroom. Whereas Car.__dict__ shows the class 
level attributes and methods."""

print(f'=======================================================================')

"""(g)Python also supports what are called magic methods or dunder (double underscore)
methods that are called automatically in response to specific operations. For example, de-
fine a function as below. and execute the statement print(str(<name-of_class)). Test
this with the above two class instances you created. For example str(toyota_camry).
What is the output? There are other magic methods such as ___iter__, __repr__ etc."""
class Car:
    showroom = 'NewAge'
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def __str__(self):
        return f"{self.year} {self.make} {self.model} in {self.color}"

toyota_camry = Car('Toyota', 'Camry', 2022, 'Red')
ford_mustang = Car('Ford', 'Mustang', 2022, 'Black')

print(str(toyota_camry))
print(str(ford_mustang))

print(f'============================================================')

"""(h)Define a static method called show_intro_message that prints the purpose of this
class. def __str__(self):
return f"{self.make} {self.model} {self.color| ({self.year})"""

class Car:
    showroom = 'NewAge'
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    @staticmethod
    def show_intro_message():
        print("This class is used to create car objects with their details.")

Car.show_intro_message()

