#created Date: feb-22/02/2022 18:45
#Python Program to Check if a Number is Odd or Even
n = int(input())
if(n%2==0):
    print(f"{n} is an even number") #f-strings
else:
    print("{0} is an Odd number".format(n)) #format strings