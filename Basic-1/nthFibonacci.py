#created Date: feb-23/02/2022 21:47
#Python Program to Print the  nth Fibonacci number

#Method-1 Iterative Approach
n = int(input())
a = 0
b = 1
temp = 0
if(n<0):
    print("can't return fibonacci number")
elif(n==0):
    print(a)
elif(n==1):
    print(b)
else:
    for i in range(2,n):
        temp = a+b
        a = b
        b = temp
    print(b)

'''
#Method-2 Recursive Approach
def fibonacci(n):
    if n<=0:
        return "can't return fibonacci"
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


n = int(input())
print(fibonacci(n))
'''
