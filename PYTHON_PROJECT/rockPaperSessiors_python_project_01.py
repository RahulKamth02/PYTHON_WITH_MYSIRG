

import random
user_choice=int(input("Enter your choice : Type 0 for Rock, 1 for paper,Type2 for Sessiors :"))

if user_choice>=3 or user_choice<0:
    print("you enter invalid num ,you loss")
else :
    computer_choice=random.randint(0,2)
print("Computer_chose:")
print(computer_choice)
if computer_choice==user_choice:
    print("It's a Draw ")

elif computer_choice==0 or user_choice==2:
    print("You loss")

elif  user_choice==0 or computer_choice==2 :
    print("You win")

elif computer_choice>user_choice:
    print("You loss")
    
elif user_choice>computer_choice:
    print("You win")

