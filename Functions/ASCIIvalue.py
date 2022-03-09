#created Date: March-9/03/2022 10:19
#Python Program to Find ASCII Value of Character
'''
ASCII stands for American Standard Code for Information Interchange.

It is a numeric value given to different characters and symbols, 
for computers to store and manipulate. For example, the ASCII value of the letter 'A' is 65.

'''

c = input()
print('ASCII value of {} is {}'.format(c, ord(c)))

print('ASCII character of {} is {}'.format(ord(c), chr(ord(c))))

#get characters from their corresponding ASCII values using the chr() function
n = int(input())
print('ASCII character of {} is {}'.format(n, chr(n)))

'''
we have used ord() function to convert a character to an integer (ASCII value). 
This function returns the Unicode code point of that character.

Unicode is also an encoding technique that provides a unique number to a character. 
While ASCII only encodes 128 characters, the current Unicode has more than 100,000 characters from hundreds of scripts.


simply, to get characters --> use chr()   --> convert an integer (ASCII value) to a character
        to get ASCII value  --> use ord() --> convert a character to an integer (ASCII value)
'''