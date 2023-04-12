from fractions import Fraction
from math import gcd

n = int(input())
dem = n // 2

dom = n - dem

while gcd(dem, dom) != 1:
    dem -= 1
    dom += 1

print(Fraction(dem, dom))
