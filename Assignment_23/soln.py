# Q1. Write a python script to calulate factorial of a given number.
num=int(input("Enter a number which num you want factorial "))
fact=1
for i in range(num,1,-1):
    fact=fact*i
print(fact)



# Q2. Write a python script to count digits in a given number.
# num=input("Enter a number :")
# digit_count=len(num)
# print("Digit count :",digit_count)




num =int(input("Enter a number :"))
count=0
while num:
    num=num//10
    count+=1
print("Digit_count=",count)




# Q3. Write a python script to calculate sum of digits of a given numbers.
num=int(input("Enter a number :"))
s=0
while num:
    r=num%10
    s=s+r
    num=num//10
print("sum =",s)



# Q4. Write a python script to print binary equivalent of a given deciamal number.(do not use bin() method)
d=int(input("Enter a number "))
s=''
while d:
    r=d%2 #1,0,0,1,1
    s=str(r)+s #1+1+0+0+1
    d=d//2 #12,6,3,1
print(s)




# Q5.Write a python script to print the octal equivalent of a given decimal number.(do not use oct() method)
d=int(input("Enter a number "))
s=''
while d:
    r=d%8 
    s=str(r)+s 
    d=d//8
print(s)
