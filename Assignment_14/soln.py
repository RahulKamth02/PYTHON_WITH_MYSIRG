# Q1. write a python script to check whether a given number is a three digit number or not.
num=int(input("Enter a number :"))
match num:
    case num:
        if num>99 and num<1000:
            print("%d is three digit num"%num)
        else:
            print("%d is not three digit num"%num)

# Q2. write a python script to check whether a given number is positive ,negative or zero.

num=int(input("Enter a number :"))
match num:
    case num if num>0:
            print("Positive")
    case num if num<0:
            print("Negative")
    case num if num==0:
            print("zero")



# Q3. write a pthon script to make a menu dirven program in which has to choose one of the otpion from four given options 1) Odd-Even ,2) Positive _Non Positive ,3) Simple interest and 4) find roots of quadratic equation .Match and execute appropriate code code on user selection.

value=eval(input("Enter a number :"))
match value:
    case 1:
        x=int(input("Enter a nuber :"))
        if x%2==0:
            print("Even")
        else:
            print("Odd")
    case 2:
        num=int(input("Enter a number :"))
        if num>0:
            print("Positive")
        elif num<0:
            print("Negative")
        else:
            print("zero")
    case 3:
        p,r,t=map(int,input("Enter principle ,rate and time separated by space :").split())
        si=p*r*t/100
        print("Simple interest is :",si)
    case 4:
        a,b,c=map(int,input("Enter a cofficient a b and c separated by space ").split())
        discriment=b**2-4*a*c
        if discriment>0:
            print("Distinct root")
        elif discriment==0:
            print("real and eaual root")
        else:
            print("imaginary root")
    





# Q4. write a python script to take one data form user and evaluate the type of data. if the data is of int type print Monday, if the data is of float type then print Tuesday,if the data is of complex type then print wednesday, if the data is of type bool then print Thursday.

value=eval(input("Enter a data :"))
match value:
    case value if type(value)==int:
        print("Monday")
    case value if type(value)==float:
        print("Tuesday")
    case value if type(value)==complex:
        print("Wednesay")
    case value if type(value)==bool:
        print("Thursday")




# Q5.Write a python script to take string form the user. if the string is a part of "mysirg" then print "one" if the string is a part of "education" then print "Two" and if the string is a part of "services" then print "Three".
# Taking user input
x = input("Enter some data: ")

# Using match statement to check the input
match x:
    case "mysrig":
        print("one")
    case "Education":
        print("two")
    case "services":
        print("three")
    case _:
        print("No match found")


    
