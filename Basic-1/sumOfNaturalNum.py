#created Date: feb-23/02/2022 22:00
#Python Program to Find the Sum of Natural Numbers

n = int(input())
total = 0
if (n<=0):
    print("can't make sum of the natural numbers with this given n")
else:
    for i in range(n+1):
        total = total+i
    print(total)
