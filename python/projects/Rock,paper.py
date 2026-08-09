# ROCK PAPER SCISSOR

import random

user_choice=int(input("0:Rock,1:Paper,3:sissor "))
computer_choice=random.randint(0,2)
print(computer_choice)
if computer_choice==user_choice:
    print("draw")
elif computer_choice>user_choice:
    print("Lose")
elif user_choice>computer_choice:
    print("Win")
elif computer_choice==0 and user_choice==2:
    print("Lose")
elif user_choice==0 and computer_choice==2:
    print("Win")