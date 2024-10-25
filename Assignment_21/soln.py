# Q1. Write a python script to print first N even natural numbers.
num=int(input("Enter a number :"))
for i in range(1,num+1):
    print(i,end=' ')
print()



# Q2. Write a python script to print first N odd natural numbers
num=int(input("Enter a number :"))
for i in range(1,num+1):
    print(i*2-1,end=' ')
print()


# Q3. Write a python script to print square of first N natural numbers.
num=int(input("Enter a number :"))
for i in range(1,num+1):
    print(i**2,end=' ')
print()


# Q4. Write a python script to print cubes of fist N natural numbers.
num=int(input("Enter a number :"))
for i in range(1,num+1):
    print(i**3,end=' ')
print()


# Q5. Write a python script to display all prime numbers within a range.

# for i in range(15,45):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=' ')
# 
#    

print("All prime Between 15 to 45 ")
for i in range(15,45):
    if i>1:
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i,end=' ')        

        # range start=15 end=45