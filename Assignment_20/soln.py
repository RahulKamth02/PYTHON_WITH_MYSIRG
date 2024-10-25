# Q1. Write a python script to print the first 10 multiples of 5
n=5
for i in range(1,11):
    # print("%d * %d =%d"%(n,i,n*i)) # 
    # print(f"{n} * {i} = {n*i}") # usng f-string method
    print("{} * {} ={}".format(n,i,n*i)) # using .format method


# Q2. Write a pythons script to print first 10 multiples of N
N=int(input("Enter a number you want to print multiple of 10 times : "))
for i in range(1,11):
    print("{} * {} ={}".format(N,i,N*i))


# Q3. Write a pthon script to print first M multiples of N.
N=int(input("Enter a number you want to multiple :"))
M=int(input("Enter a number how many times multiple of N :"))
for i in range(1,M+1):
    print("{} * {} ={}".format(N,i,N*i))


# Q4. Write a python script to print the first 10 multiples of N in reverse order
N=int(input("Enter a number you want to print multiple of 10 times : "))
for i in range(10,0,-1):
    print("{} * {} ={}".format(N,i,N*i))

# Q5. Write a python script to print table of user's choice
N=int(input("Enter a number you wnat to print table : "))
for i in range(1,11):
    print("{} * {} = {}".format(N,i,N*i))