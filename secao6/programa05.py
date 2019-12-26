"""
Faça um programa que peça para o usuário digitar 10 valores e some-os
"""
soma = 0

for num in range(1, 11):
    number = float(input(f'Digite {num}/10: '))
    soma = soma + number
print(f'A soma dos 10 números digitados foi de: {soma}')
