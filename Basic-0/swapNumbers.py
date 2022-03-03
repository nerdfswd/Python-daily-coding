#created Date: March-3/03/2022 17:34
#Python Program to swap two numbers

#method -1: Using a temporary variable
a = int(input())
b = int(input())
temp = a
a = b
b = temp
print("a= ",a, "and b = ",b)

#Method -2 : Without Using Temporary Variable
a = int(input())
b = int(input())
a, b = b,a 
print("a= ",a, "and b = ",b)

#Method -3 : Using Addition & Subtraction
a = int(input())
b = int(input())
a = a + b 
b = a - b 
a = a - b
print("a= ",a, "and b = ",b)

#Method -3 : Using Multiplication & Division
a = int(input())
b = int(input())
a = a * b 
b = a // b 
a = a // b
print("a= ",a, "and b = ",b)

#XOR swap -> This algorithm works for integers only
a = int(input())
b = int(input())
a = a ^ b 
b = a ^ b 
a = a ^ b
print("a= ",a, "and b = ",b)