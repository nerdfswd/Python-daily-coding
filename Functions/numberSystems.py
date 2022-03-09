#created Date: March-9/03/2022 10:14
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
'''In the program below, we have used anonymous (lambda) 
function inside the filter() built-in function to find all the numbers divisible by 13 in the list.

The decimal system is base 10 (ten symbols, 0-9, are used to represent a number) 
and similarly, binary is base 2, octal is base 8 and hexadecimal is base 16.


Here, built-in functions bin(), oct() and hex() are used, have to learn iterative approach...
'''
decimal = int(input())
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print(binary)
print(octal)
print(hexadecimal)

#These built-in functions take int as decimal and return output as a string