#
#
#  Funtions in python are used to create for reusability it excutes when function called and we have to create the function
#     by using Def and also with any function name:
#

# wring a function to greate

# def greet():
#     print("Hello, World")
#     print("Good morning")
# greet()

#Write a function to add two numbers and return the result

# def add(a,b):
#     return a+b
# print(add(4,4))


# Write a function to check whether a number is even or odd

# def even_odd(num):
#     if num%2==0:
#         return True
#     return False
# print(even_odd(51))
#
# print(even_odd(52))
# print(even_odd(53))
# print(even_odd(530))

# Write a function that returns the square of a number.

# def square(number):
#     return number **2
# print(square(5))
# print(square(50))


# Write a function to find the largest of two numbers.(using string formating)

# def greater(a,b=30):
#     if a>b:
#         return f"{a} is greater than {b}"
#     else:
#         return f"{b} is less than {a}"
#
# print(greater(3,4))


# Write a function to find factorial of a number.in a range

# def factorial(a):
#     if a<0:
#         return "Factors not Available"
#     else:
#         result = 1
#         for i in range(1,a+1):
#             result*=i
#         return result
# num=int(input("enter the num: "))
# print(factorial(num))


# Write a function to find factorial of a number.in a range using while loop

# def factorial(n):
#     result=1
#     i=1
#     while i<=n:
#         result*=i
#         i+=1
#     return result
# print(factorial(5))


# Write a function to check whether a number is prime.

# def prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return f"{n} is prime no."
#     else:
#         return "not a prime100."
# num=int(input("Enter a number: "))
# print(prime(num))

# write a function to convert us dollar in to INr:

# def dollar(us_dollar):
#     inr=us_dollar*83
#     return inr
#
# print(dollar(1000))


# # create fun to find len of list:
# cities=["apple","banana","orange","mango","pine"]
# def func1(list):
#     return len(list)
# print(func1(cities))
