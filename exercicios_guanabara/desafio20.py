"""
O mesmo professor do exercício anterior, quer sortear a ordem de apresentação dos trabalhos. Faça um programa que mostre
a ordem sorteada
"""
from random import shuffle

qtd = int(input('Informe a quantidade de alunos da sala: '))
vetor_alunos = []

for i in range(1, qtd + 1):
    vetor_alunos.append(str(input(f'Informe o nome do {i}° aluno(a): ')))

shuffle(vetor_alunos)

print(f'A ordem será a seguinte: {vetor_alunos}')
