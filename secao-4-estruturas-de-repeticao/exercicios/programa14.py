"""
Escreva um programa que um número inteiro positivo N e em seguida imprime N linhas do chamado triangulo de Floid.
Exemplo: N = 6
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
number = int(input('Informe um número positivo inteiro para forma o triângulo de Floid: '))

aux = 0
for i in range(0, number + 1):
    for j in range(0, number):
        if i > j:
            aux = aux + 1
            print(aux, end=' ')
    print()
