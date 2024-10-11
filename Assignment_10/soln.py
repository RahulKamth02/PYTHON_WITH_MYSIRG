# Q1 write a python script to remove the last digit from a given number.(for example if user enters 2534 then your output should be 253)

x=2534
x=x//10
print(x)

# Q2.write a python script to get the last digit from a given number.(for example if user enters 2089 then your output should be 9)

x=2089
y=2089%10
print(y)


# Q3.write a python script to swap data of two variables
x=10
y=20
temp=x
x=y
y=temp
print("x=",x,"y=",y)

# Q4.write a python script which takes a three digit number from the user and displays only its first digit

num=int(input("Enter a number :"))
num=num//100
print(num)

# Q5.write a python script which takes a three digit number from the user and displays only its middle digit
num1=int(input("Enter a number :"))
num1=num1//10
temp=num1%10
print(temp)