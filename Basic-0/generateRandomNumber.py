#created Date: March-3/03/2022 17:44
#Python Program to generate a random Number

#Using random module
'''To generate random number in Python, randint() function is used. This function is defined in random module. '''

import random
a= random.randint(0,100)
print(a)

#Here you can see a random number is generated whenever a the code is run.


#To get the same output even if u ran the code mutliple number of times use random.seed(120) here any number can be given in the brackets.

'''
The seed() method is used to initialize the random number generator.

The random number generator needs a number to start with (a seed value), to be able to generate a random number.

If you use the same seed value twice you will get the same random number twice.
'''
import random
random.seed(89)
a= random.randint(0,100)
print(a)
