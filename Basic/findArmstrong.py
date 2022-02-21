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