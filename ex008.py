met = float(input("Digite uma distância em metros: "))
km = met/1000
hm = met/100
dam = met/10
dm = met * 10
cm = met * 100
mm = met * 1000

print("A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm".format(met, km, hm, dam, dm, cm, mm))