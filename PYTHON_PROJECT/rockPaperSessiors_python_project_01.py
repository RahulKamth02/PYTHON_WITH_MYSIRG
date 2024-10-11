# Rule :-Rock win against scissors
#        scissors win agains papers
#        paper win agains rock
#        0 for Rock,2,for paper,3 for scissors 

rock = '🪨'
paper = "📃"
scissors = '✂'
gameIcons = [rock, paper, scissors]
import random

user_choice=int(input("Enter you choice : Type 0 for Rock ,1 for pape ,2 for sessiors :"))
if user_choice>3 or user_choice<0:
    print("you entered invalid choice,you loss")
else:
    computer_choice=random.randint(0,2)
    print("computer chose :")
    print(computer_choice)
    if user_choice==computer_choice:
        print("It's a draw ")
    elif computer_choice==0 and user_choice==2:
        print("you loss ")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("You loss ")
    elif user_choice>computer_choice:
        print("you win")
print("you choose :",gameIcons[user_choice])
print("computer chose :",gameIcons[computer_choice])