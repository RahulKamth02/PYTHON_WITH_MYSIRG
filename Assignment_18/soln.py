# Q1. Write a Python script to print the first N even natural numbers
n=int(input("Enter a number :"))
i=1
while i<=n:
    print(i,end=' ')
    i+=1
print()
# Q2. Write a Python script to print the first N even natural numbers in reverse order
n=int(input("Enter a number :"))
i=1
while n>=1:
    print(n,end=' ')
    n-=1
print()
# Q3. Write a python  script to print squares of first N natural numbers
n=int(input("Enter a number :"))
i=1
while i<=n:
    print(i**2,end=' ')
    i+=1
print()

# Q4. Write a python script to print cubes of first N natural numbers
n=int(input("Enter a number :"))
i=1
while i<=n:
    print(i**3,end=' ')
    i+=1
print()
# Q5.Write a python script to print first 10 multiples of N
n=int(input("Enter a num you want to print multiples "))
i=1
while i<=10:
    print("%d * %d =%d"%(n,i,n*i))
    i+=1