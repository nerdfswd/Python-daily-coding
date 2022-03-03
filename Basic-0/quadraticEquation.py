#created Date: March-2/03/2022 19:55
#Python Program to calculate the quadratic Equation

'''The standard form of a quadratic equation is:

ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
The solutions of this quadratic equation is given by:

(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) '''

import cmath
a = int(input())
b = int(input())
c = int(input())

s = (b**2 - 4*a*c)

posresult = (-b + cmath.sqrt(s))/ (2 * a)
negresult = (-b - cmath.sqrt(s))/ (2 * a)

print("{} and {}".format(posresult, negresult))