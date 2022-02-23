#created Date: feb-23/02/2022 22:16
#Python Program to Reverse a Number

#method-1: Using while loop
n = int(input())
reverse = 0
while(n>0):
    rem = n%10
    reverse = reverse*10 + rem
    n = n//10
print(reverse)

#Method-2: Using String slicing

'''
n = int(input())
n = str(n)
print(n[::-1])

'''