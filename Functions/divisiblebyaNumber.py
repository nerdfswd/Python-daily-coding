#created Date: March-9/03/2022 10:06
# Python Program to Find Numbers Divisible by Another Number
'''In the program below, we have used anonymous (lambda) 
function inside the filter() built-in function to find all the numbers divisible by 13 in the list.'''

mylist = [12, 65, 54, 39, 102, 339, 221,]
result = list(filter(lambda x: x%13==0, mylist)) #filter expects 2 arguments
print(result)


'''
filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True
syntax: filter(function, iterable)
Example 3: Using None as a Function Inside filter() - when None is used as a function , only truthy values are extracted.
'''