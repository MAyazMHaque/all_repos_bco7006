
# Parent Class 1
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def myFunction(self):
        print("Hello my name is " + self.name + " and my age is " + str(self.age))


p1 = Person("Ayaz", 29)  # instance of parent class 1
print(p1.name)
print(p1.age)
p1.myFunction()

p1.age =40
p1.myFunction()

# example 2: Parent class 2
class Person2:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
x = Person2("Ayaz","Minhaj") # creating the instance of parent class 2
x.printname()

# creating a child class of Person: inheritence when parent and child has all same properties and functions

class Student(Person):
    pass                    # any class can not be empty so just put Pass it will make twin copy of it and will inherit from Person class

y = Student("Fahad", 38)    # instance can be created with child class 1 as well.
y.myFunction()

# if you wanna add more properies in child class you need to add init function but as soon as we add it will lose inheritence
# Example 3: when child class has more properties than parent class:
class Student2(Person2):
    def __init__ (self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year
    def myChildFunction (self):
        print("Welcome " + self.fname, self.lname + " to the yaer " + str(self.graduation_year))

z = Student2("Fatimah","Ayaz",2022) # creating the instance of child class 2
print(z.fname)
print(x.fname)
z.myChildFunction()