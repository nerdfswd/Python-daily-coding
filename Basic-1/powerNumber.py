#created Date: feb-24/02/2022 16:08
#Python Program to Compute the Power of a Number

#Example 1: Calculate power of a number using a while loop
base = int(input())
exponent= int(input())
result = 1
while(exponent>0):
    result = result * base
    exponent-=1
print(result)


'''
#Example 2: Calculate power of a number using a for loop
base = int(input())
exponent= int(input())
result = 1
for i in range(exponent,0,-1):
    result = result*base
print(result)

#Example 3: Calculate the power of a number using pow() function
base = int(input())
exponent= int(input())
result = pow(base,exponent)
print(result)


'''