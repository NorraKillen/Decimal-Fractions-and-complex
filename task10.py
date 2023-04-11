from fractions import Fraction
from math import factorial
a = int(input())
k = 0
for i in range(1, a+1):
    k += Fraction(1, factorial(i))
print(k)