from math import radians, sin, cos, tan
ang = float(input("Digite um ângulo: "))

seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print("O ângulo de {} possui o SENO de {:.2f}".format(ang, seno))
print("O ângulo de {} possui o COSSENO de {:.2f}".format(ang, cos))
print("O ângulo de {} possui a TANGENTE de {:.2f}".format(ang, tan))

