mylist = list(map(int, input().split())) 
length = len(mylist)
median = 0
if(length%2==0): #[1,2,3,4]
    mid = mylist[length//2]
    median =(mid + mylist[length//2-1])//2
else:#[1,2,3,4,5]
    median = mylist[length//2]
print(median)