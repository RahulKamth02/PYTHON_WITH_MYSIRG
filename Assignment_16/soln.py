# Q1 write a python script to print first 10 even natural numbers 
i=1
while i<=10:
    print(2*i,end=' ')
    i+=1
print()


# Q2. write a python script to print first 10 even natural numbers in reverse order
i=10
while i>=1:
    print(2*i,end=' ')
    i-=1
print()

# Q3. write a python script to print square of first 10 natural numbers
i=1
while i<=10:
    print(i**2,end=' ')
    i+=1
print()
# Q4. write a python script to print cubes of first 10 natural numbers
i=1
while i<=10:
    print(i**3,end=' ')
    i+=1
print()

# Q5. Write a python script to print first 10 multiples of 5
n=5
i=1
while i<=10:
    print("%d * %d = %d"%(n,i,n*i))
    i+=1