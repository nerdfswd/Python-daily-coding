#created Date: feb-23/02/2022 19:15
#Python Program to Print the Fibonacci sequence

#Method-1 Iterative Approach
n = int(input("Enter a number to print fibonacci sequence upto n:"))
a = 0 
b = 1
temp = 0
if(n<=0):
    print("can't make a fibonacci sequence")
elif(n==1):
    print(a)
else:
    for i in range(1,n+1):
        print(a,sep=" ")
        temp = a+b
        a = b
        b = temp
'''
#Method-2 Recursive Approach
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
if(n<=0):
    print("can't make a fibonacci sequence")
else:
    for i in range(n+1):
        print(fibonacci(i))

'''