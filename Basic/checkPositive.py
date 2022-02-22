#created Date: feb-22/02/2022 18:45
#Python Program to Check if a Number is Positive, Negative or 0 
n = int(input())
if(n>=0):
    if(n==0):
        print(f"{n} is zero")
    else:
        print(f"{n} is a positive number")
else:
    print(f"{n} is a negative number")