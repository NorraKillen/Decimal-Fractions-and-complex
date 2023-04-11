from fractions import Fraction
a = int(input())
k = 0
for i in range(1, a+1):
    k += Fraction(1, i**2)
print(k)