#created Date: March-3/03/2022 18:15
#Python Program to Display Powers of 2 Using Anonymous Function
'''In the program below, we have used an anonymous (lambda) function inside the map() built-in function to find the powers of 2.'''

terms = int(input())
result = list(map(lambda x: 2**x, range(0,terms+1)))

print("Total numbers are {}".format(terms))
for i in range(0,terms+1):
    print("2 raised to the power of", i ," is ",result[i])

