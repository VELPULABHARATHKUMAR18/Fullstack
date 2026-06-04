# Find the square root of a number entered by the user.
import math
import random

# n=int(input())
# print(math.sqrt(n))
# # Find the factorial of a number.
# print(math.factorial(n))
# # Find Sin Value
# print(math.cos(math.radians(n)))


# Generate a random number between 1 and 100.

# to generate numbers we use random.randint function it gives random no from the input by importing random module

import random


print(random.randint(1,100))
# Simulate a dice roll.
print(random.randint(1,6))

# Choose a random name from a list.
l=["b","c","d","g","g"]
print(random.choice(l))

# Print current date and time.
from datetime import datetime
print(datetime.now())

# Calculate Age
# to calculate age we should do birth year-current year

# birth=int(input())
# current=datetime.now().year
#
# age=(current-birth)
# print(age)

#
# Mini Project: Number Guessing Game

# secret_num=random.randint(1,10)
#
# while True:
#     guess_num=int(input("Enter num "))
#
#     if guess_num==secret_num:
#         print("Correct Guess")
#         break
#     elif guess_num<secret_num:
#         print("near to")
#     else:
#         print("to high")

