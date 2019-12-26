"""
Faça um programa que leia 10 números inteiros positivos, ignorando não positivos, e imprima sua média
"""
cont = 0
soma = 0
media = 10

while cont != 10:
    num = float(input(f'Digite o número {cont + 1}: '))
    while num < 0:
        num = float(input(f'Digite o número {cont + 1}: '))
    soma = soma + num
    cont = cont + 1

media = (soma / media)

print(f'A média foi de: {media}')