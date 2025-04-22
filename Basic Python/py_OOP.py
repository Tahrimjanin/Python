# Define the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # The __str__() fun= str representation of the object
    def __str__(self):
        return f"{self.name}({self.age})"
    
    # greet the person
    def myfunc(self):
        print("Hello, my name is " + self.name)

#p1 of the Person class
p1 = Person("Jeny", 20)

print(p1) # the object which will use the __str__() func

p1.myfunc() # Call the myfunc() 

# Modify the age of the object
p1.age = 40
print(f"Updated age: {p1.age}")


# Delete the age property
del p1.age
# print(p1.age)  

# Delete the object p1
del p1
# print(p1)  

class EmptyClass:
    pass  


#Inheritance
# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname  # Set first name
        self.lastname = lname   # Set last name

    def printname(self):
        print(self.firstname, self.lastname)  # Print full name

# Child class inheriting from Person
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Call parent class constructor
        self.graduationyear = year      # Set graduation year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Create an object of Student
x = Student("Mike", "Olsen", 2019)
x.printname()   # Call method from parent class
x.welcome()     # Call method from child class




# Function Polymorphism


print("Function Polymorphism:")

x = "Hello World!"
print("Length of string:", len(x))

mytuple = ("apple", "banana", "cherry")
print("Length of tuple:", len(mytuple))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Length of dictionary:", len(thisdict))


# Class Polymorphism

print("\nClass Polymorphism:")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for vehicle in (car1, boat1, plane1):
    print(f"{vehicle.brand} {vehicle.model}: ", end="")
    vehicle.move()


# Inheritance + Polymorphism

print("\nInheritance Class Polymorphism:")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass  # inherits move() from Vehicle

class Boat(Vehicle):
    def move(self):
        print("Sail!")  # overrides move()

class Plane(Vehicle):
    def move(self):
        print("Fly!")  # overrides move()

car2 = Car("Toyota", "Corolla")
boat2 = Boat("Yamaha", "WaveRunner")
plane2 = Plane("Airbus", "A320")

for vehicle in (car2, boat2, plane2):
    print(f"{vehicle.brand} {vehicle.model}: ", end="")
    vehicle.move()


