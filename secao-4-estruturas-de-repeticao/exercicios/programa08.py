"""
Faça um programa que leia 10 (dez) números e escreva o maior e o menor valor lido
"""
maior = 0
menor = 0

for num in range(1, 11):
    numero = float(input(f'Digite o {num} número: '))
    if num == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f'O maior é: {maior} e o menor é {menor}')
