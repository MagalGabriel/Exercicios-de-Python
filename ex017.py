# cO = float(input("Comprimento do cateto oposto: "))
# cA = float(input("Comprimento do cateto adjacente: "))
#
# hip = (cO**2) + (cA**2)
# hip = hip ** (1/2)
#
# print("A hipotenusa vai medir {:.2f}". format(hip))

from math import hypot

cO = float(input("Comprimento do cateto oposto: "))
cA = float(input("Comprimento do cateto adjacente: "))

hip = hypot(cO, cA)

print("O comprimento da hipotenusa é {:.2f}".format(hip))

