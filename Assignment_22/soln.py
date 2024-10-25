# 1.Write a python script to calculate sum of first n natural numbers.
num=int(input("Enter a numbers :"))
s=0
for i in range(1,num+1):
    s=s+i
print(s)


# 2.Write a python script to calculate sum of square of first N natural numbers
num=int(input("Enter a numbers :"))
s=0
for i in range(1,num+1):
    s=s+(i**2)
print(s)


# 3.Write a python script to calculate sum of cubes of first N natural numbers.
num=int(input("Enter a numbers :"))
s=0
for i in range(1,num+1):
    s=s+(i**3)
print(s)


# 4.Write a python script to caluclate sum of first N odd natural numbers.
num=int(input("Enter a numbers :"))
s=0
for i in range(1,num+1):
    s=s+(2*i-1)
print(s)

# 5.Write a python script to calculate sum of first n even natural numbers
num=int(input("Enter a numbers :"))
s=0
for i in range(1,num+1):
    s=s+(2*i)
print(s)