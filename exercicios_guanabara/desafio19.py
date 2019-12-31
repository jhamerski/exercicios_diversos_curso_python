"""
O professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome escolhido.
"""
from random import choice

qtd = int(input('Informe a quantidade de alunos da sala: '))
vetor_alunos = []

for i in range(1, qtd + 1):
    vetor_alunos.append(str(input(f'Informe o nome do {i}° aluno(a): ')))

print(f'O aluno(a) escolhido foi: {choice(vetor_alunos)}')
