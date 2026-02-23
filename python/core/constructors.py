

class:
    class is nothing but it is a bluprint of objects and it contains variables and methods inside

ex:

class student()
    pass

object:
It is a instance of class
class student:
    pass
obj1=student("Bharath") -----> this is calles constructed object


constructor:
 constructor is like a machnice used to create objects  and it is a special medthod runs automatically men object is created

exx:

class student:
    def __init__(self,Name,age) :
        self.Name=Name
        self.age=age
    def display(self):
        print(self.Name)
        print(self.age)
s1=student("Bharath kumar",20)
s1.display()


ex:2

class Car:
    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
print(c1.brand)
c1.brand="Range"
print(c1.brand)

examples:

Create a class Person

Constructor should take name and age

Create a method greet() that prints:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, My name is {self.name}, and i am {self.age} years old")
person1=person("bharath",20)
 person1.greet()
per2=person("Bharghav",53)
per2.greet()

ex2:

Create a class Rectangle

Constructor takes length and width

Create methods:

area()

perimeter()

class Rectangle:
    def __init__(self,lenth,breadth):
        self.lenth=lenth
        self.breadth=breadth
    def area(self):
        return self.lenth*self.breadth
    def perimeter(self):
        return self.lenth**2+self.breadth**2
c1=Rectangle(10,10)
print(c1.area())
print(c1.perimeter())
d=Rectangle(10,150)
print(d.area())
print(d.perimeter())


Create a class Mobile

Constructor takes brand and price

Create a method details() to print both values.

class Mobile:
    def __init__(self, brand, price=79000):
        self.brand = brand
        self.price = price
    def details(self):
        print(self.brand,self.price)
d1=Mobile("samsung",8000)
d1.details()
d2=Mobile("Apple")
d2.details()


# Create a class BankAccount
#
# Constructor → account_holder, balance
#
# Methods:
#
# deposit(amount)
#
# withdraw(amount)
#
# display_balance()