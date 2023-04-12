a, z1, z2 = int(input()), complex(input()), complex(input())
z11, z22 = z1.conjugate(), z2.conjugate()
print(z1**a + z2**a + z11**a + z22**(a+1))