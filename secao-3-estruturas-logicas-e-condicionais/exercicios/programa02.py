"""
Faça um programa para verificar se um determinado número é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""
number = int(input('Digite um número para verificar se ele é divisível por 3 ou por 5: '))

if number % 3 == 0:
    print(f'O {number} é divisível por 3!')

if number % 5 == 0:
    print(f'O {number} é divisível por 5!')
