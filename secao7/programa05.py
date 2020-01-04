"""
Faça um programa que preencha um vetor de 10 números reais, calcule e mostre a quantidade de números negativos e a soma
dos positivos desse vetor
"""

lista = []

for i in range(1, 11):
    lista.append(int(input(f'Informe o {i} numero: ')))

contador = 0
soma_positiva = 0
for i in range(10):
    if lista[i] < 0:
        contador += 1
    else:
        soma_positiva = soma_positiva + lista[i]

print(f'O vetor tem {contador} números negativos. A soma dos positivos foi de: {soma_positiva}')
