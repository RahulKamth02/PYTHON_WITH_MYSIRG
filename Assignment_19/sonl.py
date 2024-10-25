# Q1. Write a python script to print each character of a string with its corresponding unicode.

str1=input("Enter a string :")
for i in str1:
    print(i,ord(i))

# Q2. Write a python script to print only vowel of the given string.
str1=input("Enter a string :")
for i in str1:
    if i in 'aeiouAEIOU':
        print(i)

# Q3. write a python script to count occurrence of spaces in a given string.
str1=input("Enter a string :")
space_count=0
for i in str1:
    if i==' ': 
        space_count+=1              #space_count=str1.count(' ')
print(space_count)


# Q4. Write a Python script to print unique digits of a given interger
num=input("Enter a number :")
u=''
for ch in num:
    if ch not in u:
        u+=ch
print(u)

# Q5. Write a python script to count number of digits in a givne number.
num=(input("Enter an number :"))
# digit_count=len(num)
digit_count=0
for i in str(num):
    if i in '0123456789':
        digit_count+=1
print("number of digit :",digit_count)

