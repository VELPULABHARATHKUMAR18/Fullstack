class Animal:
    def make_sound(self):
        print("Animal can sound")
class Dog(Animal):
    def make_sound(self):
        print("dog barks")
class cat(Animal):
    def make_sound(self):
        print("meow")
class cow(Animal):
    def make_sound(self):
        print("cow says Ambaa!")
class karthik(Animal):
    def make_sound(self):
        print("karthik says dengey")

b=[Dog(),cat(),cow(),karthik()]
for Animal in b:
    Animal.make_sound()



# Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.

# def operate(device):
#     device.start()
# class car:
#     def start(self):
#         print("car starts")
# class computer:
#     def start(self):
#         print("computer starts")
# class washingmachine:
#     def start(self):
#         print("washing macchine starts washing")
# s=car()
# operate(s)
# operate(computer())
# operate(washingmachine())


# Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.


class transport:
    def move(self):
        print("move trough transport")
class bus(transport):
    def move(self):
        print("you can travel in bus")
        super().move()
class bike(transport):
    def move(self):
        print("move trough bike")
        super().move()
t=bike()
t.move()
z=transport()
z.move()
f=bus()
f.move()

# . Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.


class payment:
    def process(self,amount):
        print(f"make payment {amount}")
class creditcard(payment):
    def process(self,amount,card_type):
        # self.amount=amount
        # self.card_type=card_type
        print(f"amount paid througn {card_type} card")
c=creditcard()
c.process(1000,"visa")
v=payment()
v.process(10000)
c.process(10,"BOI")


