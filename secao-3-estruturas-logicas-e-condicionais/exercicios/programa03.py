"""
Escreva um programa que leia dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre
ambos
"""
one = int(input('Digite um número: '))
two = int(input('Digite outro número: '))

if one > two:
    print(f'O maior número digitado foi: {one}')
    print(f'A diferença deles é: {one - two}')
else:
    print(f'O maior número digitado foi: {two}')
    print(f'A diferença deles é: {two - one}')
