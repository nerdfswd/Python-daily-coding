#created Date: feb-22/02/2022 18:52
#Python Program to Print all Prime Numbers in an Interval
lower = int(input())
upper = int(input())
for i in range(lower, upper+1):
    if i>1:
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            print(i)