# Q1.
"""num=int(input("Enter a number :"))
if num>=100 and num<=999:
    print(f"{num} is three digit number")
else:
    print(f"{num} is not three digit number")"""

# Q2.
# num=int(input("Enter a number :"))
# if num==0:
#     print("num is zero ")
# elif num>0:
#     print("Positive num ")
# elif num<0:
#     print("Negative num ")


# Q3.


# Q4.
# year=int(input("Enter a year :"))
# if year%400==0:
#     print("Leap year ")
# elif year%100==0:
#     print("Not leap year ")
# elif year%4==0:
#     print("Leap year ")
# else:
#     print("Leap year") 


# Q5.
a,b,c=map(int,input("Enter three number :").split())
if a>b and a>c:
    print("{} is greater ".format(a))
elif b>c and b>a:
    print("{} is greater ".format(b))
elif c>a and c>b:
    print("{} is greater ".format(c))