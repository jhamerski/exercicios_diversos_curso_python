"""
Faça um programa que leia um número positivo natural N e imprima todos os naturais de 0 (zero) até N em ordem crescente
"""
number = int(input('Digite um número inteiro positivo: '))

for num in range(number + 1):
    print(num)
