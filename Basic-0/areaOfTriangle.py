#created Date: March-2/03/2022 19:40
#Python Program to Find the Area of a Triangle

'''If a, b and c are three sides of a triangle. Then,

s = (a+b+c)/2
area = √(s(s-a)*(s-b)*(s-c)) '''

a = int(input())
b = int(input())
c = int(input())

#calculating semi-perimeter
s = (a+b+c)/2

area = (s*(s-a) *(s-b) * (s-c))**0.5

print(area)