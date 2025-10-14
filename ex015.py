print("=" * 10, "ALUGUEL DE CARROS", "=" * 10)

km = float(input("Quantos Km o carro rodou?: "))
dias = int(input("por quantos dias o carro foi alugado?: "))

preco = (60 * dias) + (0.15 * km)

print("Com {}Km rodados e um aluguel de {} dias, será necessário pagar R${:.2f}!".format(km, dias, preco))
