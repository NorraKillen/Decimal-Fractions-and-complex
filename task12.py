from fractions import Fraction
from math import gcd

a = set()
for i in range(1, int(input()) + 1):
    for j in range(1, i):
        a.add(Fraction(j, i))

print(*sorted(a), sep='\n')
