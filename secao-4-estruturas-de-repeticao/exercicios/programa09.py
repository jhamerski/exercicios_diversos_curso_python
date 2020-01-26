"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros naturais ímpares
"""
numero = int(input('Informe um número positivo:'))

for num in range(1, numero+1):
    if num % 2 != 0:
        print(num)
