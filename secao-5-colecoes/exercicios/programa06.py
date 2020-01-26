"""
Leia duas matrizes 2X2 e escreva uma terceira matriz com os maiores valores valores de cada posição das matrizes lidas
"""
matriz = [[0, 0], [0, 0]]
matriz_dois = [[0, 0], [0, 0]]
matriz_result = [[0, 0], [0, 0]]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = (int(input(f'Matriz 1: Informe o elemento [{i} {j}]: ')))

for i in range(len(matriz_dois)):
    for j in range(len(matriz_dois)):
        matriz_dois[i][j] = (int(input(f'Matriz 2: Informe o elemento [{i} {j}]: ')))

print('-=' * 30)
print('MATRIZ ORIGINAL 1')
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print('-=' * 30)
print('MATRIZ ORIGINAL 2')
for i in range(len(matriz_dois)):
    for j in range(len(matriz_dois)):
        print(f'[{matriz_dois[i][j]:^5}]', end='')
    print()

for i in range(2):
    for j in range(2):
        if matriz[i][j] >= matriz_dois[i][j]:
            matriz_result[i][j] = matriz[i][j]
        else:
            matriz_result[i][j] = matriz_dois[i][j]

print('-=' * 30)
print('MATRIZ RESULTADO')
for i in range(2):
    for j in range(2):
        print(f'[{matriz_result[i][j]:^5}]', end='')
    print()
