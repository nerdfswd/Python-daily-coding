#created Date: feb-24/02/2022 19:52
#Python Program to Find the Square Root

#Example: For positive numbers
n= int(input())
result = n **0.5
print(result)

#Example: For positive numbers
n = float(input())
result = n**0.5
print("%.3f"%(result))

#For real or complex numbers
import cmath
n= eval(input())
result = cmath.sqrt(n)
print(result)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(n,result.real,result.imag))