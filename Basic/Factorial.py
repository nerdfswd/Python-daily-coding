#created Date: feb-22/02/2022 18:52
#Python Program to Find the Factorial of a Number

#Method-1 Iterative approach
n = int(input())
factorial = 1
if(n<0):
    print("Factorial not exists")
elif(n==0 or n==1):
    factorial = 1
    print(factorial)
else:
    for i in range(1,n+1):
        factorial = factorial * i 
    print(factorial)

#Method-2 Recursive approach
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

n = int(input())
print(factorial(n))


'''