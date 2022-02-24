#created Date: feb-24/02/2022 16:08
#Python Program to Find Armstrong Number in an Interval

'''A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...    '''


lowerLimit = int(input())
upperLimit = int(input())

for n in range(lowerLimit, upperLimit+1):
    length = len(str(n))
    temp = n
    result = 0
    while(n>0):
        rem = n%10
        result = result + rem ** length
        n = n//10
    if(result == temp):
        print(f"{temp} is an armstrong number")
    

