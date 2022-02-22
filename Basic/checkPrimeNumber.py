#created Date: feb-22/02/2022 18:52
#Python Program to Check Prime Number
#Method-1: using "flag"
n = int(input())
flag = False
if(n>1):
    for i in range(2,n):
        if n%i == 0:
            flag = True
            break
if(flag):
    print("{} is not a prime number".format(n))
else:
    print("{} is a prime number".format(n))

#Method-2: using "for loop"
'''
# Program to check if a number is prime or not

num = int(input())

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")


'''