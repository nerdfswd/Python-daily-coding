#created Date: feb-22/02/2022 18:52
#Python Program to Find the Largest Among Three Numbers
a = int(input())
b = int(input())
c = int(input())
if(a>b and a>c):
    print("{} is greater".format(a)) #.format is used here.. ;)
elif(b>c and b>a):
    print("{} is greater".format(b))
else:
    print("{} is greater".format(c))