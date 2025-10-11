real = float(input("Quanto dinheiro você tem na carteira?: R$"))

dolar = real / 5.34
iene = real * 27.6

print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
print("Com R${:.2f} você pode comprar JP¥{:.2f}".format(real, iene))