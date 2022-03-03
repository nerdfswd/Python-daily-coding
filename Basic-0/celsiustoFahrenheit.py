#created Date: March-3/03/2022 18:00
#Python Program to convert Celsius to Fahrenheit

'''In the program below, we take a temperature in degree Celsius and convert it into degree Fahrenheit. They are related by the formula:

fahrenheit = celsius * 1.8 + 32 '''


celsius = float(input())
fahrenheit = celsius * 1.8 + 32
print("%.2f degrees celsius is equal to %.2f degrees fahrenheit" %(celsius, fahrenheit))