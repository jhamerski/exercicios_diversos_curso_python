"""
Leia um vetor de 10 posições, e atribua o número 0 (zero) para números negativos.
"""
vetor = []
valor = 0

for i in range(1, 11):
    valor = int(input(f'Informe o {i}° valor: '))
    if valor < 0:
        vetor.append(0)
    else:
        vetor.append(valor)

print(vetor)
