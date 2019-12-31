"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
"""
number = int(input('Digite um número para saber a sua tabuada: '))

for i in range(1, 11):
    aux = i * number
    print(f'{i} X {number} = {aux}')