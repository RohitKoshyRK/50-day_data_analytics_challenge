# %%
#Q1 - Create a class Dog with:
#An attribute name.
#A method bark that prints: "Woof! My name is <name>".

# %%
#A1 - 

class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"Woof! My name is {self.name}")

my_dog = Dog("Kaiser Chokli")
my_dog.bark()

# %%
#Q2 - Create a class called Cat that has:
# An attribute color.
# A method meow that prints: "Meow! I am a <color> cat."

# %%
class Cat:

    def __init__(self, color):
        self.color=color

    def meow(self):
        print(f"Meow! I am a {self.color} cat")


my_cat = Cat("grey")
my_cat.meow()

# %%
#Q3 - Create a class called Car that has:
# Two attributes: brand and year.
# A method called info that prints:
#"This car is a <brand> from <year>."

# %%
class Car:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"This car is {self.brand} from {self.year}")


my_car = Car("Toyota",2020)
my_car.info()

# %%
#Q4 - Create a class called Book that has:
# Two attributes: title and author.
# A method called details that prints:
# "The book '<title>' is written by <author>."

# %%
#A4 - 

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def details(self):
        print(f"The book {self.title} is written by {self.author}")

my_book = Book("Harry Potter", "JK Rowling")
my_book.details()


# %%
## Q5 - Create a class called Student that has:
# Three attributes: name, age, and grade.
# A method called show_info that prints:
#"Student: <name>, Age: <age>, Grade: <grade>"

# %%
class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")


student1 = Student("Raj",12,"A")
student1.show_info()
        

# %%
# Q6 - Create a class called Movie that has:
# Three attributes: title, director, and year.
# A method called summary that prints:
# "'<title>' directed by <director> was released in <year>."

# %%
#A6 -

class Movie:

    def __init__(self,title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def summary(self):
        print(f"{self.title} directed by {self.director} was released in {self.year}")

movie1 = Movie("Titanic","James Cameron","1995")
movie1.summary

# %%
#Q7 - learning __str__

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    

book1 = Book("HP","JKR")
print(book1)


# %%
# Q8 - Create a class called Laptop with:
# Three attributes: brand, model, and price.
# A __str__() method that returns:
# "Laptop: <brand> <model> - $<price>"

# %%
class Laptop():

    def __init__(self, brand,model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Laptop: {self.brand} {self.model} - INR {self.price}"
    

laptop1 = Laptop("Dell","XPS 14", 56000)
print(laptop1)

# %%
# Q9 - Class: Vehicle
# Attribute: brand
# Method: start_engine() → prints "Engine started."

# Class: Car (inherits from Vehicle)
# Attribute: model (in addition to brand)
# Override the start_engine() method to print:
#"Car <brand> <model>'s engine is now running."

# %%
#A9 -

class Vehicle():

    def __init__(self,brand):
        self.brand=brand

    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):

    def __init__(self,brand, model):
        super().__init__(brand) # Inherit brand from Vehicle
        self.model=model # Add new attribute
    
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine is now runnning.")

v = Vehicle("Yamaha")
v.start_engine()

c = Car("Toyota","Corolla")
c.start_engine()

# %%
# A10 - You're building a simulation of electronic devices. 
# Create a base class called Device and a child class called Smartphone.
"""
Requirements:

The Device class should have:

An __init__ method that takes a brand parameter.

A method called power_on() that prints:
"Device is now powered on."

The Smartphone class should inherit from Device, and:

Its __init__ method should take two parameters: brand and model, and use super() to initialize brand.

It should override the power_on() method to print:
"<brand> <model> is now powered on and ready to use."

Create:

One instance of Device with brand "GenericTech" and call power_on().

One instance of Smartphone with brand "Apple" and model "iPhone 15" and call power_on().

"""

# %%
class Device():

    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print("Device is now powered on.")


class Smartphone(Device):

    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is now powered on and ready to use.")

    def take_photo(self):
        print(f"Photo taken with {self.brand} {self.model}")


tech1 = Device("GenericTech")
tech1.power_on()

tech2 = Smartphone("Apple","iPhone 15")
tech2.power_on()
tech2.take_photo()

# %%
# Q 11 - Problem Statement:
# Create a class called Book to represent a book in a library system.
# Requirements:
"""
/Add an __init__ method with title and author.
/Add an instance method display_info() to print:
/"Title: <title>, Author: <author>
/Add a class variable library_name with value "Central Library".
/ Add a class method change_library_name(cls, new_name) to update the library name.
Add a static method is_valid_isbn(isbn) that:
Returns True if the ISBN is a 13-digit number.
Returns False otherwise.
"""

# %%
class Book():

    library_name = "Central Library" # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

    @classmethod
    def change_library_name(cls, new_name): #Class method
        cls.library_name = new_name

    @staticmethod
    def is_valid_isbn(isbn): #Static method
        return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()



b1 = Book("1984", "George Orwell")
b1.display_info()

# %%
print(Book.library_name)  # Central Library
Book.change_library_name("City Library")
print(Book.library_name)  # City Library

# %%
print(Book.is_valid_isbn("9783161484100"))  # True
print(Book.is_valid_isbn("12345"))          # False

# %%
# Q12 - Practice Question: Class and Static Methods

"""
/Problem Statement:
/Create a class called Employee that tracks employees in a company.
/Requirements:
/Each employee has a name and position.
/The company has a shared company_name which is "TechCorp" by default.
/Create an instance method show_details() that prints:
/"Name: <name>, Position: <position>, Company: <company_name>"
/Create a class method change_company_name(cls, new_name) to change the shared company name.
/Create a static method is_valid_email(email) that:
Returns True if the email contains "@" and "."
Returns False otherwise
"""

# %%
class Employee():
    
    company_name = "TechCorp" # class variable

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self): #Instance method
        print(f"Name: {self.name}, Position: {self.position}, Company: {Employee.company_name}")

    @classmethod
    def change_company_name(cls, new_name): #Class method
        cls.company_name = new_name

    @staticmethod
    def is_valid_email(email): # Static method
        return "@" in email and "." in email
    

# %%
e1 = Employee("Alice", "Engineer")
e1.show_details()

# %%
Employee.change_company_name("InnoSoft")
e2 = Employee("Bob", "Manager")
e2.show_details()
# Expected: Name: Bob, Position: Manager, Company: InnoSoft
e1.show_details()
# Expected: Name: Alice, Position: Engineer, Company: InnoSoft


# %%
print(Employee.is_valid_email("user@example.com"))  # True
print(Employee.is_valid_email("test.user@domain.co"))  # True

# %%
print(Employee.is_valid_email("userexample.com"))  # False (missing @)
print(Employee.is_valid_email("user@domaincom"))   # False (missing .)
print(Employee.is_valid_email("userdomain.com"))   # False (missing @)
print(Employee.is_valid_email("@."))               # True 

# %%
## Q14 - Imagine you have different types of animals, and each animal can make a sound. You want:
"""
Encapsulation: The animal’s name should be private, not accessible directly.
Polymorphism: Each animal makes a different sound when you call the make_sound() method.
Abstraction: You want to enforce that all animals must have a make_sound() method.
"""

# %%
from abc import ABC, abstractmethod

#Abstract base class - Animal

class Animal(ABC):
    def __init__(self,name):
        self.__name = name # Encapsulation: name is private

    def get_name(self):
        return self.__name # Accessor method for the name
    
    @abstractmethod #Sub-classes must implement this
    def make_sound(self):
        pass 

## Dog class inherits from Animal
class Dog(Animal):
    def make_sound(self):
        print(f"{self.get_name()} says : Woof!")

## Cat class inherits from Animal
class Cat(Animal):
    def make_sound(self):
        print(f"{self.get_name()} says : Meow!")


# %%
dog = Dog("Buddy")
cat = Cat("Whiskers")


dog.make_sound()  # Buddy says: Woof!
cat.make_sound()  # Whiskers says: Meow!

# %%
#Q14 - Create a class structure for vehicles:
"""
/ An abstract Vehicle class with a private attribute __speed.

/Two subclasses: Car and Bicycle.

/Both must implement a method called move() that prints a message about how they move.

Ensure speed is encapsulated and only accessible through a getter method.

"""

# %%
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self,speed):
        self.__speed = speed #Encapsulation

    def get_speed(self):
        return self.__speed
    
    @abstractmethod
    def move():
        pass
    
class Car(Vehicle):
    def move(self):
        print(f"The car moves at {self.get_speed()} km/h on roads.")

class Bicycle(Vehicle):
    def move(self):
        print(f"The bike pedals along at {self.get_speed()} km/h")

# %%
def test_vehicles():
    car = Car(100)
    bike = Bicycle(25)

    print("Testing Car:")
    print("Speed:", car.get_speed())  # Should print 100
    car.move()                        # Should describe how the car moves

    print("\nTesting Bicycle:")
    print("Speed:", bike.get_speed())  # Should print 25
    bike.move()                        # Should describe how the bicycle moves

if __name__ == "__main__":
    test_vehicles()


# %%


# %%


# %%



