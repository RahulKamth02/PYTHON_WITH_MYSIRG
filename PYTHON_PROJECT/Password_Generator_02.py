import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number=['0','1','2','3','4','5','6','7','8','9']

symbol=['!','@','#','%','^','&','*','(',')','-','+']
print("Welcome to password generator  ")
n_letter=int(input("How many latter you want in your password :"))
n_number=int(input("How many number you want in your password :"))
n_symbol=int(input("How many symbol you want in your password :"))
passwrod_list=[]
for i in range(1,n_letter+1):
    char=random.choice(letters)
    passwrod_list+=char
for i in range(1,n_number+1):
    char=random.choice(number)
    passwrod_list+=char
for i in range(1,n_symbol+1):
    char =random.choice(symbol)
    passwrod_list+=char
print(passwrod_list)
random.shuffle(passwrod_list)
print(passwrod_list)
password=""
for char in passwrod_list:
    password+=char
print(password)