"""
Faça um programa que receba 3 números e mostre em ordem crescente.
"""
lista = []

for i in range(3):
    lista.append(float(input(f'Informe o {i + 1}° número: ')))

lista.sort()
print(lista)
