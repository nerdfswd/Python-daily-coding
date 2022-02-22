''' created Date: feb-22/02/2022 18:45
A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...
'''

n = int(input())
length = len(str(n))
temp = n
total = 0
while(temp>0):
    rem = temp%10
    total+=rem**length
    temp = temp//10
if(total==n):
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number')