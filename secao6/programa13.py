"""
Faça um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17, após um número dado
"""
one = int(input('Digite um número inteiro: '))

while one != 0:
    one = one + 1
    if one % 11 == 0 or one % 13 == 0 or one % 17 == 0:
        print(f'O número {one} é multiplo de 11 ou 13 ou 17')
        one = 0
