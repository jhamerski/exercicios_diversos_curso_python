"""
Leia um vetor de 10 posições. Contar e escrever quantos pares ele possui
"""
vetor = [[], []]
valor = 0
contador = 0

for i in range(1, 11):
    valor = int(input(f'Informe o {i}° valor: '))
    if valor % 2 == 0:
        vetor[0].append(valor)
        contador += 1

print(f'Os valores pares são {vetor[0]} e tem {contador} números pares.')
