import random

alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special=['@','#','$','%','&','(',')']



n_alphabets=int(input("enter: "))
n_numbers=int(input("enter the no: "))
n_special=int(input("enter: "))
password=[]
for i in range(1,n_alphabets+1):
    chars=random.choice(alphabets)
    password+=chars
for j in range(1,n_numbers+1):
    nums=random.choice(numbers)
    password+=nums
for k in range(1,n_special+1):
    spec=random.choice(special)
    password+=spec
random.shuffle(password)# using random.shuffle we can easily shuffle the whole list and it is a in-built function.
for i in password:# to print as string from the list
    print(i,end="")