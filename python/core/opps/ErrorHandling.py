# # 1. Person class with age validation
# class Person:
#     def __init__(self, age):
#         if age < 0:
#             raise ValueError("Age cannot be negative.")
#         self.age = age
#
#
# # 2. find_length function
# def find_length(obj):
#     try:
#         count = 0
#         for _ in obj:
#             count += 1
#         return count
#     except TypeError:
#         print("Error: An integer is not iterable, so its length cannot be calculated.")
#
#
# # 3. Student class with marks validation
# class Student:
#     def __init__(self):
#         self.marks = None
#
#     def set_marks(self, marks):
#         if not (0 <= marks <= 100):
#             raise ValueError("Marks must be between 0 and 100.")
#         self.marks = marks
#
#
# # 4. Custom InvalidAgeError and Voter class
# class InvalidAgeError(Exception):
#     pass
#
# class Voter:
#     def check_eligibility(self, age):
#         if age < 18:
#             raise InvalidAgeError("Age must be at least 18 to vote.")
#
#
# # 5. BankAccount with withdraw validation
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise Exception("Insufficient balance.")
#         self.balance -= amount
#
#
# # 6. PasswordValidator class
# class PasswordValidator:
#     def validate(self, password):
#         if len(password) < 8:
#             raise ValueError("Password must be at least 8 characters long.")
#
#
# # 7. UserInput class with separate except blocks
# class UserInput:
#     def get_integer(self, value):
#         try:
#             return int(value)
#         except ValueError:
#             print("ValueError: Cannot convert this value to an integer.")
#         except TypeError:
#             print("TypeError: Invalid type provided.")
#
#
# # 8. Shape base class and Rectangle child class
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement the area() method.")
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# # 9. Service class catching exception from another method
# class Service:
#     def risky_method(self):
#         raise Exception("Something went wrong in risky_method.")
#
#     def run(self):
#         try:
#             self.risky_method()
#         except Exception as e:
#             print(f"Caught in Service: {e}")
#
#
# # 10. Transaction class with try, except, finally
# class Transaction:
#     def process(self):
#         try:
#             print("Processing transaction...")
#             # Simulate work
#         except Exception as e:
#             print(f"Transaction failed: {e}")
#         finally:
#             print("Cleanup: Transaction process ended.")
#
#
# 11. LoginSystem with exception handled outside the class
class LoginSystem:
    def login(self, password):
        if password != "secret123":
            raise Exception("Incorrect password.")
        print("Login successful.")

# Usage:
system = LoginSystem()
try:
    system.login("wrongpass")
except Exception as e:
    print(f"Login error: {e}")