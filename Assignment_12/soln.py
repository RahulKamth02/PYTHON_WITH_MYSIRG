# Q1
# num=int(input("Enter a number :"))
# if num>0:
#     print("Positive num ")
# else :
#     print("Non Positive num ")


# Q2.
# num=int(input("Enter a number  :"))
# if num%5==0:
#     print("Num is divisible by 5")
# else:
#     print("Num is not divisible by 5")


# Q3.
# num=int(input("Enter a number :"))
# if num%2==0:
#     print("Even num ")
# else:
#     print("Odd num ")

# Q4.
# a,b=map(int,input('Enter two number :').split())
# if a==b:
#     print("same num")
# elif a>b:
#     print("{} is greater ".format(a))
# else :
#     print("{} is greater ".format(b))


# Q5
# write a python script to print two given wors in dictionary order
word1=input("Enter the first word :")
word2=input("Enter the second word :")
if word1>word2:
    print("Dictionary order is {word1},{word2}")
elif word2>word1:
    print("Dictionary order is {word2},{word1}")
else:
    print("Both word are the same :")
