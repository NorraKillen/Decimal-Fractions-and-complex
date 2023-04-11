from fractions import Fraction

num1 = input()
num2 = input()
num3 = Fraction(num1)
num4 = Fraction(num2)

print(num1, '+', num2, '=', num3 + num4)
print(num1, '-', num2, '=', num3 - num4)
print(num1, '*', num2, '=', num3 * num4)
print(num1, '/', num2, '=', num3 / num4)