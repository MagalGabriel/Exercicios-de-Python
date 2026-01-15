import random

alunos = []

a1 = input("Digite o nome do primeiro aluno: ")
alunos.append(a1)
a2 = input("Digite o nome do segundo aluno: ")
alunos.append(a2)
a3 = input("Digite o nome do terceiro aluno: ")
alunos.append(a3)
a4 = input("Digite o nome do quarto aluno: ")
alunos.append(a4)

selec = random.choice(alunos)

print("O aluno escolhido foi {}".format(selec))
