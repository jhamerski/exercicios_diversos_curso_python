"""
Faça um programa que leia 10 inteiros e imprima sua média
"""
soma = 0
media = 10

for num in range(1, 11):
    number = float(input(f'Digite {num}/10: '))
    soma = soma + number
media = (soma / media)

print(f'A média foi de: {media}')
