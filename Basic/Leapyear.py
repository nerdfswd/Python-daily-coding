#created Date: feb-22/02/2022 18:45
#Python Program to Check Leap Year 
year = int(input())
if((year%400==0) and (year%100 ==0)):
    print(f"{year} is a leap year")
elif((year%4==0) and (year%100!=0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")