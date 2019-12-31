"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, e os escreva na tela
"""
vetor = []
iguais = []

for i in range(1, 11):
    vetor.append(int(input(f'Informe o {i}° elemento: ')))

for i in range(1, 11):
    for j in range(1, 11):
        if vetor[i] == vetor[j]:
            iguais.append(vetor[i])

print(iguais)
