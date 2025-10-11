larg = float(input("Largura da parede: "))
altu = float(input("Altura da parede: "))

area = larg * altu
tintaNec = area / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, altu, area))
print("Para pintar essa parede você vai precisar de {}l de tinta. ". format(tintaNec))