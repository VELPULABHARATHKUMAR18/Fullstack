# Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.

class peerson:
    def __init__(self,age):

        if age<0:
            raise ValueError("Age must be greater than zero")
        self.age=age
p=peerson(30)
print(p.age())



