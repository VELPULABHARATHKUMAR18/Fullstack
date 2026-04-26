#  1, Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
#
#
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# a=Animal()
# b=Dog()
# a.sound()
# b.sound()
#
#
# 2.
#  Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super().
#
# class A:
#     def show(self):
#         print('it shows')
# class B(A):
#     def show(self):
#         super().show()
#         print("doe not shows")
# Obj=B()
# Obj.show()
#
#
# 3.
#  Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.
#
# class A:
#     def display(self):
#         print("Displays A")
# class B(A):
#     def display(self):
#         # super().display()
#         print("Displays B")
# class C(B):
#     def display(self):
#         # super().display()
#         print("Displays C")
# obj=C()
# obj.display()
# obj2=B()
# obj2.display()
#
#
# 4: Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().
#
# class vehicle:
#     def info(self):
#         print("wheels is 2 or 4")
# class Car(vehicle):
#     def wheels(self):
#         # super().wheels()
#         print("Wheels is 4")
# class bike(vehicle):
#     def wheels(self):
#         # super().wheels()
#         print("wheels is 2")
# a=bike()
# b=Car()
# a.info()
# a.wheels()
# b.wheels()
#
#
#  5. Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs.
#
# class Employee:
#     def salary(self):
#         print("employee salary is 20000")
# class manager(Employee):
#     def salary(self):
#         # super().salary()
#         basic=20000
#         incentives=6000
#         total=basic+incentives
#         print(f"Manager total salary is {total}")
# a=manager()
# a.salary()
# b=Employee()
# b.salary()
#
#
# 6. Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.
#
#
# class university:
#     uni_name="Jntuh"
#     @classmethod
#     def show(cls):
#         print(f"college name is", cls.uni_name)
# class College(university):
#     def display(self):
#         print("college belongs to",self.uni_name)
# b=College()
# # b.display()
# # b.show()
# # print(b.uni_name)
# university.show()
# b.display()
#
#
#  7. Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.
#
#
# class mathops:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#
# class advops(mathops):
#     pass
# r=advops()
# r.add(10,20)
# d=mathops()
# d.add(50,60)
#
# 8.: Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO
#
#
class father:
    def skills(self):
        print("outside work")
class mother:
    def skills(self):
        print("Home work")
class child(father,mother):
    pass
a=child()
a.skills()
a.skills()
print(child.mro())
#
#
#  10 Create class Person with a constructor __init__(name). Create class
# Student(Person) with constructor __init__(name, roll). Use super() to call the
# parent constructor
#
#
# class person:
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
# class student(person):
#     def __init__(self,name,rollno):
#
#         self.rollno=rollno
#         super().__init__(name)
#         print(self.rollno)
# a=student("bharath",20)
#
# b=student("kumar",50)


#
#
#
# Create a class Animal with a method sound().
# Create a child class Dog that overrides the method.


# class Animal:
#     def sound(self):
#         print("Animal Makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog has 4 legs")
# b=Animal()
# b.sound()


# Create a class Person with attributes name and age.
# Create a child class Student with an extra attribute marks.


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class student(person):
#     def __init__(self,name,age,marks):
#         self.marks=marks
#         super().__init__(name,age)
#     def display(self):
#         print("my name is", self.name)
#         print( "my age is", self.age)
#         print("I got", self.marks)
# name=str(input())
# age=int(input())
# marks=int(input())
#
# st1=student(name,age,marks)
# st1.display()

# Create a class Vehicle with method start().
# Create a class Car that inherits from Vehicle


# class vehicle:
#     def start(self):
#         print("vehicle has 2 0r 4 wheels")
# class car(vehicle):
#     def start(self):
#         print("car has 4 wheels")
#     def bike(self):
#         print("bike has 2 wheels")
#
# bmw=car()
# bmw.bike()


#
# Create a class Shape with method area().
# Create a class Circle that calculates area


# class shape:
#     def area(self):
#         return none
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         result=3.14*self.radius*self.radius
#         print(result)
# radius=int(input())
# c=circle(20)
# c.area()




# Create a class Employee with attributes name and salary.
# Create a subclass Manager with an extra attribute department.
#
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class manager:
#     def __init__(self,department):
#         self.department=department
#         super().__init__(name,salary,department)
